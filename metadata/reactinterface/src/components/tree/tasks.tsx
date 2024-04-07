import * as React from 'react';
import {
    TreeItem,
    TreeItemProps,
    useTreeItem,
    TreeItemContentProps,
  } from '@mui/x-tree-view/TreeItem';
  
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