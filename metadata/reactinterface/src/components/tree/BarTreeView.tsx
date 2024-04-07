import * as React from 'react';
import { styled, alpha } from '@mui/material/styles';
import { TreeView } from '@mui/x-tree-view/TreeView';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import {
  TreeItem,
  TreeItemProps,
  useTreeItem,
  TreeItemContentProps,
} from '@mui/x-tree-view/TreeItem';
import clsx from 'clsx';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

import Stack from '@mui/material/Stack';
import IconButton  from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';
import AddCircleTwoToneIcon from '@mui/icons-material/AddCircleTwoTone';
import CopyAllTwoToneIcon from '@mui/icons-material/CopyAllTwoTone';
import {CustomContentRoot} from './CustomContentRoot'

import {Catalog,Catalogs} from './catalogs'

import myStructure from './firststructure.json'

const CustomContent = React.forwardRef(function CustomContent(
  props: TreeItemContentProps,
  ref,
) 
{
  const {
    className,
    classes,
    label,
    nodeId,
    icon: iconProp,
    expansionIcon,
    displayIcon,
  } = props;

  const {
    disabled,
    expanded,
    selected,
    focused,
    handleExpansion,
    handleSelection,
    preventSelection,
  } = useTreeItem(nodeId);

  const icon = iconProp || expansionIcon || displayIcon;

  const handleMouseDown = (event: React.MouseEvent<HTMLDivElement, MouseEvent>) => {
    preventSelection(event);
  };

  const handleClick = (event: React.MouseEvent<HTMLDivElement, MouseEvent>) => {
    handleExpansion(event);
    handleSelection(event);
  };

  return (
    <CustomContentRoot
      className={clsx(className, classes.root, {
        'Mui-expanded': expanded,
        'Mui-selected': selected,
        'Mui-focused': focused,
        'Mui-disabled': disabled,
      })}
      onClick={handleClick}
      onMouseDown={handleMouseDown}
      ref={ref as React.Ref<HTMLDivElement>}
    >
      <div className="MuiTreeItem-contentBar" />
      <div className={classes.iconContainer}>{icon}</div>
      <Typography component="div" className={classes.label}>
        {label}
      </Typography>
    </CustomContentRoot>
  );
});

const CustomTreeItem = React.forwardRef(function CustomTreeItem(
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) {
  
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});


export default function BarTreeView({currentTreeId, setCurrentTreeId}) {
  const myStructure2 = [1,2,3,4,5,6]
  const handleChange = (event: React.SyntheticEvent<Event, Event>, nodeIds: Array<T> | string):void => {
    console.log(nodeIds);
    setCurrentTreeId(nodeIds);
    
  };

  return (
    <Box sx={{ minHeight: 180, flexGrow: 1, maxWidth: 400, textAlign: 'left'  }}>

      <Stack direction="row" spacing={1}>
        <IconButton aria-label="add">
          <AddCircleTwoToneIcon/>
        </IconButton>
        <IconButton aria-label="copy">
          <CopyAllTwoToneIcon/>
        </IconButton>



      </Stack>

      <TreeView
        aria-label="icon expansion"
        defaultCollapseIcon={<ExpandMoreIcon />}
        defaultExpandIcon={<ChevronRightIcon />}
        onNodeSelect={handleChange}
        sx={{ position: 'relative' }}
      >
        <CustomTreeItem nodeId="Applications" label="Applications">
          <CustomTreeItem key={999} nodeId="Applications.MyApp" label="MyApp">
          
      
          </CustomTreeItem>

          {myStructure.map( (itemApp, index)=>
            (<CustomTreeItem key={index} nodeId= {'Applications.'+itemApp.Application} label={itemApp.Application}>
                <Catalogs></Catalogs>
            </CustomTreeItem>)
            )
          
          }


        </CustomTreeItem>

      </TreeView>
    </Box>
  );
}
/*

      <Catalogs nodeId="Applications.MyApp.Catalogs" label="Catalogs" >
              <Catalog nodeId="Applications.MyApp.Catalogs.Goods" label="Goods" >
                  <Properties nodeId="Applications.MyApp.Catalogs.Goods.Properties" label="Properties" />
                  <Tabulars nodeId="Applications.MyApp.Catalogs.Goods.Tabulars" label="Tabulars" />
                  <Forms nodeId="Applications.MyApp.Catalogs.Goods.Forms" label="Forms" />
                  <Templates nodeId="Applications.MyApp.Catalogs.Goods.Templates" label="Templates" />
              </Catalog>

              <Catalog nodeId="Applications.MyApp.Persons" label="Persons">
                  <Properties nodeId="Applications.MyApp.Persons.Properties" label="Properties" />
                  <Tabulars nodeId="Applications.MyApp.Persons.Tabulars" label="Tabulars" />
                  <Forms nodeId="Applications.MyApp.Persons.Forms" label="Forms" />
                  <Templates nodeId="Applications.MyApp.Persons.Templates" label="Templates" />

              </Catalog>

              <Catalog nodeId="Applications.MyApp.Catalogs.Warehouses" label="Warehouses" />
              <Catalog nodeId="Applications.MyApp.Catalogs.Departments" label="Departments" />

            </Catalogs>
          
            <Documents nodeId="Applications.MyApp.Documents" label="Documents" />
            <InformationRegisters nodeId="Applications.MyApp.InformationRegisters" label="Information registers" />
            <AccumulationRegisters nodeId="Applications.MyApp.AccumulationRegisters" label="Accumulation registers" />
            <Constants nodeId="Applications.MyApp.Constants" label="Constants" />
            <DataProcessors nodeId="Applications.MyApp.DataProcessors" label="Data processors" />
            <Reports nodeId="Applications.MyApp.Reports" label="Reports" />
            <Tasks nodeId="Applications.MyApp.Tasks" label="Tasks" />


*/
