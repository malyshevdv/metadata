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



const CustomContentRoot = styled('div')(({ theme }) => ({
  WebkitTapHighlightColor: 'transparent',
  '&&:hover, &&.Mui-disabled, &&.Mui-focused, &&.Mui-selected, &&.Mui-selected.Mui-focused, &&.Mui-selected:hover':
    {
      backgroundColor: 'transparent',
    },
  '.MuiTreeItem-contentBar': {
    position: 'absolute',
    width: '100%',
    height: 24,
    left: 0,
  },
  '&:hover .MuiTreeItem-contentBar': {
    backgroundColor: theme.palette.action.hover,
    // Reset on touch devices, it doesn't add specificity
    '@media (hover: none)': {
      backgroundColor: 'transparent',
    },
  },
  '&.Mui-disabled .MuiTreeItem-contentBar': {
    opacity: theme.palette.action.disabledOpacity,
    backgroundColor: 'transparent',
  },
  '&.Mui-focused .MuiTreeItem-contentBar': {
    backgroundColor: theme.palette.action.focus,
  },
  '&.Mui-selected .MuiTreeItem-contentBar': {
    backgroundColor: alpha(
      theme.palette.primary.main,
      theme.palette.action.selectedOpacity,
    ),
  },
  '&.Mui-selected:hover .MuiTreeItem-contentBar': {
    backgroundColor: alpha(
      theme.palette.primary.main,
      theme.palette.action.selectedOpacity + theme.palette.action.hoverOpacity,
    ),
    // Reset on touch devices, it doesn't add specificity
    '@media (hover: none)': {
      backgroundColor: alpha(
        theme.palette.primary.main,
        theme.palette.action.selectedOpacity,
      ),
    },
  },
  '&.Mui-selected.Mui-focused .MuiTreeItem-contentBar': {
    backgroundColor: alpha(
      theme.palette.primary.main,
      theme.palette.action.selectedOpacity + theme.palette.action.focusOpacity,
    ),
  },
}));

const CustomContent = React.forwardRef(function CustomContent(
  props: TreeItemContentProps,
  ref,
) {
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

const Catalogs = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Catalog = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});


const Properties = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Property = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});



const Forms = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Form = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});



const Tabulars = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Tabular = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});


const Templates = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Template = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});


const Documents = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Document = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});


const InformationRegisters = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const InformationRegister = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Constants = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Constant = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});



const Reports = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Report = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});



const Tasks = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem  ContentComponent={CustomContent} {...props} ref={ref} />;
});

const Task = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});


const AccumulationRegisters = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const AccumulationRegister = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});



const DataProcessors = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});

const DataProcessor = React.forwardRef((
  props: TreeItemProps,
  ref: React.Ref<HTMLLIElement>,
) => {
  return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});






export default function BarTreeView({currentTreeId, setCurrentTreeId}) {

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
          <CustomTreeItem nodeId="Applications.MyApp" label="MyApp">
          
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

          </CustomTreeItem>

        </CustomTreeItem>
      </TreeView>
    </Box>
  );
}