import * as React from 'react';
import {
    TreeItem,
    TreeItemProps,
    useTreeItem,
    TreeItemContentProps,
  } from '@mui/x-tree-view/TreeItem';
  
export const Forms = React.forwardRef((
    props: TreeItemProps,
    ref: React.Ref<HTMLLIElement>,
  ) => {
    return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
  });
  
export const Form = React.forwardRef((
    props: TreeItemProps,
    ref: React.Ref<HTMLLIElement>,
  ) => {
    return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
  });