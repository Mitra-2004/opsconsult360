' OpsConsult 360 | Create native PivotTables in Excel for Mac or Windows.
' Run on a COPY of the workbook. This macro is NOT executed by the GitHub pipeline.
' Excel 365 / Excel 2021 or later recommended. Existing workbook sheets are preserved.
Option Explicit

Public Sub CreateOpsConsultPivotTables()
    Dim wb As Workbook
    Set wb = ThisWorkbook
    Application.ScreenUpdating = False
    On Error GoTo Failed

    CreatePivot wb, "Project Portfolio", "Native Pivot - Delivery", "ptDelivery", _
        "Department", "Status", "Project ID", "Projects", xlCount, "", "", 0

    CreatePivot wb, "Project Portfolio", "Native Pivot - Finance", "ptFinance", _
        "Department", "", "Planned Cost YTD", "Planned Cost (INR)", xlSum, _
        "Actual Cost YTD", "Actual Cost (INR)", xlSum

    CreatePivot wb, "Resource Allocation", "Native Pivot - Resources", "ptResources", _
        "Department", "", "Hours Logged", "Logged Hours", xlSum, _
        "Assigned Capacity", "Available Hours", xlSum

    Application.ScreenUpdating = True
    MsgBox "Three genuine PivotTables created. Verify against COO Review and Excel QA.", vbInformation
    Exit Sub
Failed:
    Application.DisplayAlerts = True
    Application.ScreenUpdating = True
    MsgBox "PivotTable creation stopped: " & Err.Description & vbCrLf & _
        "Check the source headers and workbook permissions.", vbExclamation
End Sub

Private Sub CreatePivot(ByVal wb As Workbook, ByVal sourceName As String, _
    ByVal destinationName As String, ByVal pivotName As String, ByVal rowField As String, _
    ByVal columnField As String, ByVal metric1 As String, ByVal label1 As String, _
    ByVal summary1 As XlConsolidationFunction, ByVal metric2 As String, _
    ByVal label2 As String, ByVal summary2 As XlConsolidationFunction)

    Dim sourceSheet As Worksheet, destination As Worksheet
    Dim sourceRange As Range, cache As PivotCache, pt As PivotTable

    Set sourceSheet = wb.Worksheets(sourceName)
    Set sourceRange = sourceSheet.Range("A6").CurrentRegion

    On Error Resume Next
    Set destination = wb.Worksheets(destinationName)
    On Error GoTo 0
    If Not destination Is Nothing Then
        ' Only remove sheets previously created by this macro, not original MIS reports.
        Application.DisplayAlerts = False
        destination.Delete
        Application.DisplayAlerts = True
    End If

    Set destination = wb.Worksheets.Add(After:=wb.Worksheets(wb.Worksheets.Count))
    destination.Name = destinationName
    destination.Range("A1").Value = "OPSCONSULT 360  /  " & pivotName
    destination.Range("A2").Value = "Synthetic data | Refresh via Data > Refresh All"

    Set cache = wb.PivotCaches.Create(SourceType:=xlDatabase, _
        SourceData:=sourceSheet.Name & "!" & sourceRange.Address(ReferenceStyle:=xlR1C1))
    Set pt = cache.CreatePivotTable(TableDestination:=destination.Range("A4"), _
        TableName:=pivotName)
    With pt
        .PivotFields(rowField).Orientation = xlRowField
        .PivotFields(rowField).Position = 1
        If Len(columnField) > 0 Then
            .PivotFields(columnField).Orientation = xlColumnField
            .PivotFields(columnField).Position = 1
        End If
        .AddDataField .PivotFields(metric1), label1, summary1
        If Len(metric2) > 0 Then .AddDataField .PivotFields(metric2), label2, summary2
        .RowAxisLayout xlTabularRow
        .DisplayFieldCaptions = True
    End With
    destination.Columns("A:J").AutoFit
End Sub
