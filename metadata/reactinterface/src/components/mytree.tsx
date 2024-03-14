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

export default function BarTreeView() {
  return (
    <Box sx={{ minHeight: 180, flexGrow: 1, maxWidth: 300 }}>
      <TreeView
        aria-label="icon expansion"
        defaultCollapseIcon={<ExpandMoreIcon />}
        defaultExpandIcon={<ChevronRightIcon />}
        sx={{ position: 'relative' }}
      >
        <CustomTreeItem nodeId="Applications" label="Applications">
          <CustomTreeItem nodeId="Catalogs" label="Catalogs" >
            <CustomTreeItem nodeId="CatalogsGoods" label="Goods" >
                <CustomTreeItem nodeId="Properties" label="Properties" />
                <CustomTreeItem nodeId="Tabulars" label="Tabulars" />
                <CustomTreeItem nodeId="Forms" label="Forms" />
                <CustomTreeItem nodeId="Templates" label="Templates" />
            </CustomTreeItem>

            <CustomTreeItem nodeId="CatalogsPersons" label="Persons">
                <CustomTreeItem nodeId="Properties" label="Properties" />
                <CustomTreeItem nodeId="Tabulars" label="Tabulars" />
                <CustomTreeItem nodeId="Forms" label="Forms" />
                <CustomTreeItem nodeId="Templates" label="Templates" />

            </CustomTreeItem>

            <CustomTreeItem nodeId="CatalogsWarehouses" label="Warehouses" />
            <CustomTreeItem nodeId="CatalogsDepartments" label="Departments" />

          </CustomTreeItem>
          
          <CustomTreeItem nodeId="Documents" label="Documents" />
          <CustomTreeItem nodeId="InformationRegisters" label="Information registers" />
          <CustomTreeItem nodeId="AccumulationRegisters" label="Accumulation registers" />
          <CustomTreeItem nodeId="Constants" label="Constants" />
          <CustomTreeItem nodeId="DataProcessors" label="Data processors" />
          <CustomTreeItem nodeId="Reports" label="Reports" />
          <CustomTreeItem nodeId="Tasks" label="Tasks" />

        </CustomTreeItem>
        <CustomTreeItem nodeId="5" label="Documents">
          <CustomTreeItem nodeId="10" label="OSS" />
          <CustomTreeItem nodeId="6" label="MUI">
            <CustomTreeItem nodeId="8" label="index.js" />
          </CustomTreeItem>
        </CustomTreeItem>
      </TreeView>
    </Box>
  );
}