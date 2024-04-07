import * as React from 'react';
import {
    TreeItem,
    TreeItemProps,
    useTreeItem,
    TreeItemContentProps,
  } from '@mui/x-tree-view/TreeItem';


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