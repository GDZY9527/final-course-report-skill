param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
    [string]$Version = 'v0.1.0'
)

$ErrorActionPreference = 'Stop'

$dist = Join-Path $Root 'dist'
$stage = Join-Path $dist "final-course-report-$Version"
$zip = Join-Path $dist "final-course-report-$Version.zip"

Write-Host 'This script creates a release zip candidate.'
Write-Host 'Review exclusions before using the zip for submission or distribution.'
Write-Host ''
Write-Host 'Default exclusions:'
Write-Host '  - .git, dist, __pycache__, node_modules, build caches'
Write-Host '  - docx/pdf/zip/rar/7z outputs'
Write-Host '  - executables, object files, logs, temp files, env files'
Write-Host ''

if (Test-Path -LiteralPath $stage) {
    Remove-Item -LiteralPath $stage -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $stage | Out-Null
New-Item -ItemType Directory -Force -Path $dist | Out-Null

$excludeDirNames = @('.git', 'dist', '__pycache__', 'node_modules', 'build', 'CMakeFiles')
$excludeExt = @('.docx', '.pdf', '.zip', '.rar', '.7z', '.exe', '.obj', '.pdb', '.ilk', '.log', '.tmp')
$excludeNames = @('.env')

$files = Get-ChildItem -LiteralPath $Root -Recurse -File | Where-Object {
    $relativeParts = $_.FullName.Substring($Root.Length).TrimStart('\') -split '\\'
    $skipDir = $false
    foreach ($part in $relativeParts) {
        if ($excludeDirNames -contains $part) {
            $skipDir = $true
            break
        }
    }
    -not $skipDir -and
    ($excludeExt -notcontains $_.Extension.ToLowerInvariant()) -and
    ($excludeNames -notcontains $_.Name)
}

foreach ($file in $files) {
    $relative = $file.FullName.Substring($Root.Length).TrimStart('\')
    $target = Join-Path $stage $relative
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
    Copy-Item -LiteralPath $file.FullName -Destination $target
}

if (Test-Path -LiteralPath $zip) {
    Remove-Item -LiteralPath $zip -Force
}
Compress-Archive -LiteralPath $stage -DestinationPath $zip

Write-Host "RELEASE_ZIP_CREATED: $zip"
