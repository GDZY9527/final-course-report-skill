param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'

$required = @(
    'AGENTS.md',
    'README.md',
    '.gitignore',
    'skills/final-course-report/SKILL.md',
    'references/report_workflow.md',
    'references/smart_defaults.md',
    'references/project_contract.md',
    'references/frontend_quality.md',
    'references/visual_rules.md',
    'references/environment.md',
    'references/delivery_quality.md',
    'references/originality_and_sources.md',
    'references/course_patterns.md',
    'references/portability.md',
    'references/report_density.md',
    'references/template_adaptation.md',
    'references/platform_failures.md',
    'references/execution_log.md',
    'references/project_uniqueness.md',
    'references/frontend_design.md',
    'references/docx_formatting.md',
    'references/chengdu_neusoft_report_standard.md',
    'references/chengdu_neusoft_report_standard.zh-CN.md',
    'references/appendix_policy.md'
)

$missing = @()
foreach ($item in $required) {
    $path = Join-Path $Root $item
    if (-not (Test-Path -LiteralPath $path)) {
        $missing += $item
    }
}

$riskyPatterns = @(
    '\b\d{11}\b',
    'OPENAI[_-]?API[_-]?KEY\s*=',
    ('s' + 'k-[A-Za-z0-9]'),
    ('BEGIN ' + 'PRIVATE KEY')
)

$hits = @()
$scanFiles = Get-ChildItem -LiteralPath $Root -Recurse -File |
    Where-Object {
        $_.FullName -notmatch '\\\.git\\' -and
        $_.Name -ne 'validate_portability.ps1' -and
        $_.Extension -in @('.md', '.yaml', '.yml', '.txt', '.ps1', '.json')
    }

foreach ($file in $scanFiles) {
    $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
    foreach ($pattern in $riskyPatterns) {
        if ($text -match $pattern) {
            $hits += [pscustomobject]@{
                File = $file.FullName
                Pattern = $pattern
            }
        }
    }
}

if ($missing.Count -gt 0) {
    Write-Host 'PORTABILITY_CHECK_FAIL: missing files'
    $missing | ForEach-Object { Write-Host "  - $_" }
    exit 1
}

if ($hits.Count -gt 0) {
    Write-Host 'PORTABILITY_CHECK_WARN: possible private data or secret patterns'
    $hits | ForEach-Object { Write-Host "  - $($_.Pattern) in $($_.File)" }
    exit 2
}

Write-Host 'PORTABILITY_CHECK_PASS'
