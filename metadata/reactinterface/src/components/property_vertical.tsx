import * as React from 'react';
import Box from '@mui/material/Box';

import {
    GridRowsProp,
    GridRowModesModel,
    GridRowModes,
    DataGrid,
    GridColDef,
    GridToolbarContainer,
    GridActionsCellItem,
    GridEventListener,
    GridRowId,
    GridRowModel,
    GridRowEditStopReasons,
  } from '@mui/x-data-grid';

  const columns: GridColDef[] = [
    { field: 'propertyname', 
      headerName: 'Property name', 
      width: 180, 
      //editable: true 
    },
    {
      field: 'value',
      headerName: 'Value',
      //type: 'number',
      width: 200,
      align: 'center',
      //headerAlign: 'left',
      //editable: false,
    },
   
  ]

  const initialRows: GridRowsProp = [
    {
      id: 1,
      propertyname: "Name",
      value: 'fvfvfvfv',
    },
    {
      id: 2,
      propertyname: "Description",
      value: 'ffff',
    }
  ]

  interface EditToolbarProps {
    setRows: (newRows: (oldRows: GridRowsProp) => GridRowsProp) => void;
    setRowModesModel: (
      newModel: (oldModel: GridRowModesModel) => GridRowModesModel,
    ) => void;
  }

  

export function PropertyVertical({currentTreeId}){
  const [rows, setRows] = React.useState(initialRows)


  React.useEffect(()=>{
    //need to read request from frontend structure and show to user

  let idItems = currentTreeId.split('.'); 
  let idItemsLength = idItems.length;

  
  if ((idItemsLength == 1) || (idItemsLength == 3) || (idItemsLength == 5)) {
    setRows([]);
  }

  if (idItemsLength == 2) {
    const initialRows: GridRowsProp = [
      {
        id: 1,
        propertyname: "Name",
        value: idItems[idItemsLength-1],
      },
      {
        id: 2,
        propertyname: "Description",
        value: '',
      },
      {
        id: 3,
        propertyname: "Path",
        value: '/' + idItems[idItemsLength-1],
      }
    ]
    setRows(initialRows)
    
  }


  if (idItemsLength == 4) {
    const initialRows: GridRowsProp = [
      {
        id: 1,
        propertyname: "Name",
        value: idItems[idItemsLength-1],
      },
      {
        id: 2,
        propertyname: "Description",
        value: '',
      },
      {
        id: 3,
        propertyname: "TableName",
        value: '',
      }
    ]
    setRows(initialRows)
    
  }



}, [currentTreeId])



return (

<>
  <h2>{currentTreeId}</h2>
  
  <Box sx={{ width: '30rem' }}>
  <DataGrid
        rows={rows}
        columns={columns}
        editMode="row"
        showColumnVerticalBorder = 'true'
        showCellVerticalBorder = 'true'
        hideFooterSelectedRowCount = 'true'
        hideFooterPagination = 'true'
        //rowModesModel={rowModesModel}
        //onRowModesModelChange={handleRowModesModelChange}
        //onRowEditStop={handleRowEditStop}
        //processRowUpdate={processRowUpdate}
        
        //slots={{
        //  toolbar: EditToolbar,
        //}}
        //slotProps={{
        //  toolbar: { setRows, setRowModesModel },
        //}}
      />

</Box>

</>




)






}