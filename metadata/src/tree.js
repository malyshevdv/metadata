//import  from {/metadata/src/myhttp}

class TreeClass {
    constructor (name) {
        this.name = name;
        
        this.showBar = false;
        this.selectedItem = undefined;
        this.mydata = {} //takeDateFromSite(siteAdr) ;
        this.needRedrawTree = false;
        this.list_id = [];
        this.JSON_string = '';
        this.NextCount = 0;
    }

    get_list_id() {
        return this.list_id; 
    }        
    getNextID() {
        this.NextCount += 1
        return this.NextCount
    }
    pushItem(Item, returnNextID = true){
        let newName = '' + Item;
        if (returnNextID) {
            newName = newName + '.' + this.getNextID() ;
        }
        this.list_id.push(newName) ;
        
        return newName  
    }

}

function SelectCursor(myId) {

    document.getElementById("ss").innerHTML = myId;
    dd = document.getElementById(myId);
    
    if (dd.getAttribute('opened') === 'false') {
        dd.setAttribute('opened', "true");
        
        for (itemId of mytree1.list_id) {
            if (itemId.search(myId) === 0) {
                dd = document.getElementById(itemId);
                dd.style.display = 'flex';
            }
            
        }

    }
    else {
        dd.setAttribute('opened', "false");

        for (itemId of mytree1.list_id) {
            if (itemId.search(myId) === 0) {
                dd = document.getElementById(itemId);
                dd.style.display = 'none';
            }
            
        }   

    }    
    
}
        
function SelectItem(myId){
            
    //document.getElementById("ss").innerHTML = "" + myId + "{{ url_for('metadata', path='/menu.css') }}";
    //updateForm('<div>Hello word</div>') 

    dd = document.getElementById(myId);
    let ss = 4;
    
    if (dd.getAttribute('selected') === 'false') {
        dd.setAttribute('selected', 'true');
    }
    
    clearSelection(myId);    

    ShowProperty_Action(myId);
  
}
       

function clearSelection(ExeptId){

    for (let myId of mytree1.list_id) {
        if (myId === ExeptId) {
            res = 0;
        }
        else {
            var myElement = document.getElementById(myId);
            if ((myElement != null) && (myElement.getAttribute('selected')==='true')){
                myElement.setAttribute('selected','false');
            }
        }
        
    }
}


function RedrawTree(myTree) {

    container = document.getElementById(myTree.name);
    if (container === undefined) {
        return
    }

    TreeID = myTree.name;
    

    // MENU


    menu_bar = document.createElement('div');
    menu_bar.className = 'bar-top'
    
    menu_bar_item = document.createElement('div');
    menu_bar_item.className = 'bar-item';
    menu_bar_item.innerHTML = 'Create';
    menu_bar_item.setAttribute('OnClick', 'Tree_Menu_Create(id)');
    menu_bar_item.setAttribute('id', TreeID + '.menu.create');
    
    menu_bar.appendChild(menu_bar_item);

    container.appendChild(menu_bar);



    //ELEMENTS

    root_el = document.createElement('div');
    root_el.setAttribute('name', 'TreeID.root');
    root_el.innerHTML = '<a>root</a>';

    let MetadataTypes = ["Catalogs" , "Documents", "InformationRegisters"];

    let nextID = myTree.getNextID();

    for (MetadataType of MetadataTypes) {
        FullName0 = TreeID + '.'+MetadataType;
        
        MetadataTypeElem = DrawFirstLevelElement(container, MetadataType, MetadataType, 1, FullName0);
        MetadataItems = myTree.mydata[MetadataType];
        for (MetadataItem_Index in MetadataItems) {
            MetadataItem = MetadataItems[MetadataItem_Index]
            MetadataItemName = MetadataItem.Properties.Name.Value;
            FullName1 = FullName0 + '.'+ MetadataItemName;
            ItemStruct = {
                'FieldName': TreeID, 
                'MetadataType' : MetadataType,
                'MetadataName' : MetadataItemName,
                'ItemType' : '',
                'PropertyName' : '',
                'LevelType' : '',
                'LevelPropName' : ''
            }
             
            elem_catalog = DrawFirstLevelElement(MetadataTypeElem, MetadataItemName, MetadataItemName, 0, FullName1,"0", MetadataType,'CatalogItem');
        
            //reg - dimensions and resourses    

            if (['InformationRegisters'].includes(MetadataType)) {
                //Dimensions
               SubGroup = 'Dimensions';
               FullName2 = FullName1 + '.' + SubGroup;
               elem_atr = DrawFirstLevelElement(elem_catalog, SubGroup, SubGroup, 0, FullName2);
   
               for (SubItem_Index in MetadataItem[SubGroup]) {
                   SubItem = MetadataItem[SubGroup][SubItem_Index]
                   SubItemName = SubItem.Name;
                   FullName3 = FullName2 + '.' + SubItem.Name;
                   DrawFirstLevelElement(elem_atr, SubItemName, SubItemName, 0, FullName3,"-1" , SubGroup);
               }
                    
                //Resourses
               SubGroup = 'Resourses';
               FullName2 = FullName1 + '.' + SubGroup;
               elem_atr = DrawFirstLevelElement(elem_catalog, SubGroup, SubGroup, 0, FullName2);
   
               for (SubItem_Index in MetadataItem[SubGroup]) {
                   SubItem = MetadataItem[SubGroup][SubItem_Index]
                   SubItemName = SubItem.Name;
                   FullName3 = FullName2 + '.' + SubItem.Name;
                   DrawFirstLevelElement(elem_atr, SubItemName, SubItemName, 0, FullName3,"-1" , SubGroup);
               }
   
                    
                }
   

            //Attributes
            SubGroup = 'Attributes';
            FullName2 = FullName1 + '.' + SubGroup;
            elem_atr = DrawFirstLevelElement(elem_catalog, SubGroup, SubGroup, 0, FullName2);

            for (SubItem_Index in MetadataItem[SubGroup]) {
                SubItem = MetadataItem[SubGroup][SubItem_Index]
                SubItemName = SubItem.Name.Value;
                FullName3 = FullName2 + '.' + SubItemName;
                DrawFirstLevelElement(elem_atr, SubItemName, SubItemName, 0, FullName3,"-1" , SubGroup);
            }


            //TabularSections
            //if (['Catalogs', 'Documens'].includes((x) => x === MetadataType)) {
            if (['Catalogs', 'Documents'].includes(MetadataType) ) {
                    SubGroup = 'TabularSections';
                FullName2 = FullName1 + '.' + SubGroup;
                elem_atr = DrawFirstLevelElement(elem_catalog, SubGroup, SubGroup, 0, FullName2);

                for (SubItem_Index in MetadataItem[SubGroup]) {
                    SubItem = MetadataItem[SubGroup][SubItem_Index]
                    SubItemName = SubItem.Properties.Name.Value;
                    FullName3 = FullName2 + '.' + SubItemName;
                    elem_tab = DrawFirstLevelElement(elem_atr, SubItemName, SubItemName, 0, FullName3,"-1" , SubGroup);
            
                    for (keySubItemAtr in SubItem['Attributes']) {
                        SubItemAtr = SubItem['Attributes'][keySubItemAtr];
                        SubItemAtrName = SubItemAtr.Name.Value;
                        FullName4 = FullName3 + '.Attributes.' + SubItemAtrName;
                        DrawFirstLevelElement(elem_tab, SubItemAtrName, SubItemAtrName, '', FullName4,"-1" , "Attributes");
                    }        
                }
            }   
        
            //Forms
            SubGroup = 'Forms';
            FullName2 = FullName1 + '.' + SubGroup;
            elem_atr = DrawFirstLevelElement(elem_catalog, SubGroup, SubGroup, 0, FullName2);

            for (SubItem_Index in MetadataItem[SubGroup]) {
                SubItem = MetadataItem[SubGroup][SubItem_Index]
                SubItemName = SubItem.Name.Value;
                FullName3 = FullName2 + '.' + SubItemName;
                DrawFirstLevelElement(elem_atr, SubItemName, SubItemName, 0, FullName3,"-1" , SubGroup);
            }

        
            //Commands
            SubGroup = 'Commands'
            FullName2 = FullName1 + '.' + SubGroup;
            elem_atr = DrawFirstLevelElement(elem_catalog, SubGroup, SubGroup, 0, FullName2);

            for (SubItem_Index in MetadataItem[SubGroup]) {
                SubItem = MetadataItem[SubGroup][SubItem_Index]
                SubItemName = SubItem.Name.Value;
                FullName3 = FullName2 + '.' + SubItemName;
                DrawFirstLevelElement(elem_atr, SubItemName, SubItemName, 0, FullName3,"-1" , SubGroup);
            }


            //Templates
            SubGroup = 'Templates'
            FullName2 = FullName1 + '.' + SubGroup;
            elem_atr = DrawFirstLevelElement(elem_catalog, SubGroup, SubGroup, 0, FullName2);

            for (SubItem_Index in MetadataItem[SubGroup]) {
                SubItem = MetadataItem[SubGroup][SubItem_Index]
                SubItemName = SubItem.Name.Value;
                FullName3 = FullName2 + '.' + SubItemName;
                DrawFirstLevelElement(elem_atr, SubItemName, SubItemName, 0, FullName3,"-1" , SubGroup);
            }

        } //Item
    }    

    

    //alert('sdsd')
    myTree.needRedrawTree = false;
    

} //RedrawTree


    

function DrawFirstLevelElement(rootElement, Name, Title, levelNumber, FullName, SubItemsCount='0', NameIcon = '', ItemType) {

    let FullNameItems = FullName.split('.');
    let ItemName = "" + FullNameItems[0]+'.Item' ;
    let nextID = mytree1.pushItem(ItemName)
    
    root_catalog = document.createElement('div');
    root_catalog.className = 'tree-item';
    rootElement.appendChild(root_catalog);

    root_catalog1 = document.createElement('div');
    root_catalog1.className = 'tree-level-padding-' + levelNumber;
    root_catalog.appendChild(root_catalog1);

    if (SubItemsCount === '-1') {
    }
    else {
       root_catalog2 = document.createElement('div')
        root_catalog2.className = 'tree-cursor'
        root_catalog2.setAttribute('opened', 'true')
        root_catalog2.setAttribute('id', nextID + '.',)
        root_catalog2.setAttribute('OnClick', 'SelectCursor(id)',)
        root_catalog2.setAttribute('SubItemsCount', SubItemsCount)
        root_catalog.appendChild(root_catalog2)
    }    

    root_catalog3 = document.createElement('div');
    if (NameIcon === '') { 
        root_catalog3.className = 'tree-' + Name + '-icon'
    }
    else { 
        root_catalog3.className = 'tree-' + NameIcon + '-icon'
    }
    
    root_catalog.appendChild(root_catalog3)

    root_catalog4 = document.createElement('div')
    root_catalog4.id = Name
    root_catalog4.className = 'tree-item  group-vertical'
    root_catalog4.setAttribute('id', nextID + '.gr')
    root_catalog4.setAttribute('SubItemsCount', SubItemsCount)
    
   // root_catalog4.innerHTML = Title;

    span = document.createElement('span')
    span.innerHTML = Title;
    span.setAttribute('id', nextID)
    span.setAttribute('selected', 'false')
    span.setAttribute('OnClick', 'SelectItem(id)')
    span.setAttribute('SubItemsCount', SubItemsCount)
    span.setAttribute('ItemType', ItemType)

    for (let ii=0; ii < FullNameItems.length; ii++){
        span.setAttribute('id'+ii, FullNameItems[ii]);
    }
    span.setAttribute('id_level', FullNameItems.length-1);
    span.setAttribute('id_count', FullNameItems.length);
    


    root_catalog4.setAttribute('id', nextID + '.root')
    
    root_catalog4.appendChild(span);

    root_catalog.appendChild(root_catalog4)
 
    rootElement.appendChild(root_catalog)

    return root_catalog4;
}

function DrawCatalogItemElement(nextID, rootElement, item, Name, Title, levelNumber)  {
    DrawFirstLevelElement(nextID, rootElement, 'Catalogs', item.Name, levelNumber)  
}

function Tree_Menu_Create(id) {
    //container = document.getElementById(id);
    //words = id.split();
    alert('Create');

}