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


  const initialRows: GridRowsProp = [
    {
      id: 1,
      name: "Name",
      value: 25,
    },
    {
      id: 2,
      name: "Description",
      value: 36,
    }
  ]

  interface EditToolbarProps {
    setRows: (newRows: (oldRows: GridRowsProp) => GridRowsProp) => void;
    setRowModesModel: (
      newModel: (oldModel: GridRowModesModel) => GridRowModesModel,
    ) => void;
  }

  

export function MyProperty(){

return (

<>
<p>My property</p>
</>



)






}