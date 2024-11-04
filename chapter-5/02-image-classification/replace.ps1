$storageAcct = 'ai102str193837986'
(Get-Content training-images/training_labels.json) -replace '<storageAccount>', $storageAcct | Out-File training-images/training_labels.json