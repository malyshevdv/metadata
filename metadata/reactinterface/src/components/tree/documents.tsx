import * as React from 'react';
import {
    TreeItem,
    TreeItemProps,
    useTreeItem,
    TreeItemContentProps,
  } from '@mui/x-tree-view/TreeItem';


export const Documents = React.forwardRef((
    props: TreeItemProps,
    ref: React.Ref<HTMLLIElement>,
  ) => {
    return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});
  
export const Document = React.forwardRef((
    props: TreeItemProps,
    ref: React.Ref<HTMLLIElement>,
  ) => {
    return <TreeItem ContentComponent={CustomContent} {...props} ref={ref} />;
});
  