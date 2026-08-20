# ==============================================================================
# Auto-Update README.md Directory Structure (ASCII Safe Version)
# ==============================================================================

# 1. Fetch filtered repository items
$excludedItems = @('.git', '__pycache__', '*.pyc', 'md', 'Prompts', '.gitignore', '.github', '*.tmp', '*.ps1')
$items = Get-ChildItem -Path . | Where-Object { 
    $itemName = $_.Name
    $isExcluded = $false
    foreach ($pattern in $excludedItems) {
        if ($itemName -like $pattern) { $isExcluded = $true; break }
    }
    return -not $isExcluded
} | Sort-Object PSIsContainer -Descending

# 2. Build clean ASCII directory tree string using safe ASCII pipes
$treeLines = [System.Collections.Generic.List[string]]::new()
$treeLines.Add("PersonaGenerator/")

for ($i = 0; $i -lt $items.Count; $i++) {
    $isLast = ($i -eq $items.Count - 1)
    $prefix = if ($isLast) { "\-- " } else { "|-- " }
    $suffix = if ($items[$i].PSIsContainer) { "/" } else { "" }
    $treeLines.Add("${prefix}$($items[$i].Name)${suffix}")
}

$treeOutput = ($treeLines -join "`n")

# 3. Read existing README.md content
$readmePath = "README.md"
if (-not (Test-Path $readmePath)) {
    Write-Host "Error: $readmePath not found in working directory." -ForegroundColor Red
    exit
}
$readmeContent = Get-Content -Path$readmePath -Raw -Encoding UTF8

# 4. Perform Regex replacement on the ```text ... ``` code block
$pattern = "(?s)```text\r?\nPersonaGenerator/.*?\r?\n```"
$replacementBlock = "```text`n$treeOutput`n```"

if ($readmeContent -match$pattern) {
    $updatedReadme =$readmeContent -replace $pattern,$replacementBlock
    [System.IO.File]::WriteAllText((Get-Item $readmePath).FullName, $updatedReadme, [System.Text.Encoding]::UTF8)
    Write-Host "SUCCESS: README.md directory structure successfully synchronized!" -ForegroundColor Green
} else {
    Write-Host "WARNING: Could not match '```text PersonaGenerator/... ```' block in README.md." -ForegroundColor Yellow
}