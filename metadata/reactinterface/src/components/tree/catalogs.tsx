import * as React from 'react';
import {
    TreeItem,
    TreeItemProps,
    useTreeItem,
    TreeItemContentProps,
  } from '@mui/x-tree-view/TreeItem';
import {CustomContentRoot} from './CustomContentRoot'
  
    
//CATALOGS
export const Catalogs = React.forwardRef((
    props: TreeItemProps,
    ref: React.Ref<HTMLLIElement>,
  ) => {
    
    return (
    <TreeItem ContentComponent={CustomContent} {...props} ref={ref} label="Catalogs" />

    )
  });
  
  
export const Catalog = React.forwardRef((
    props: TreeItemProps,
    ref: React.Ref<HTMLLIElement>,
  
  ) => {
    
    return (
    <TreeItem ContentComponent={CustomContent} {...props} ref={ref}>
    </TreeItem>
    )  
  });