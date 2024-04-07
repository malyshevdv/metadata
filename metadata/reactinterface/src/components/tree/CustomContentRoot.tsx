
import { styled, alpha } from '@mui/material/styles';

export const CustomContentRoot = styled('div')(({ theme }) => ({
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