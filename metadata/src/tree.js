//import {MyHelloTree2} from "./src/metadata.js"
//utils = require("./metadata");

function MyHelloTree(){
    const utils = await import("./src/metadata.js");
    utils.MyHelloTree2();
    //alert('MyHello from Tree') 
}

class Metadata{

    constructor(){
        this.Catalogs = Object<Catalog>{};
        this.Documents = Object<Document>{};
        this.InformationRegisters = Object<InformationRegister>{};
    }

}

class MetadataObject{
    constructor(Name, metadata){
        this.Name = Name;
        this.RootMetadata = metadata;
    }
    rename(Newname){
        this.Name = Newname;
    }
    getPropertyList(){
        res = []
        return res;
    }

}

class Catalog extends MetadataObject {
    constructor(){
        pass
    }
    
    NewObject(){

    }

}


class Document extends MetadataObject {
    constructor(){
        pass
    }

}

class InformationRegister extends MetadataObject {
    constructor(){
        pass
    }

}

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
    
    mytree1.selectedItem = myId;

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

function drawMenuButton(parentContainer, CommandName, ShowTitle = true){

    menu_bar_item = document.createElement('div');
    menu_bar_item.className = 'bar-item';
    menu_bar_item.setAttribute('id', TreeID + '.menu.create');
    menu_bar_item.Title = 'Delete'
    
    img = document.createElement('img');
    
    if (CommandName === 'Delete') {
        img.setAttribute('src','/metadata/images/delete.png')
        menu_bar_item.setAttribute('OnClick', 'Tree_Menu_Delete(id)');
        menu_bar_item.setAttribute('title', 'Delete object');
    }
    if (CommandName === 'Create') {
        img.setAttribute('src','/metadata/images/create.png')
        menu_bar_item.setAttribute('OnClick', 'Tree_Menu_Create(id)');
        menu_bar_item.setAttribute('title', 'Create object');
    }
    if (CommandName === 'MoveUp') {
        img.setAttribute('src','/metadata/images/arrow-up.png')
        menu_bar_item.setAttribute('OnClick', 'Tree_Menu_MoveUp(id)');
        menu_bar_item.setAttribute('title', 'Move object UP');
    }
    if (CommandName === 'MoveDown') {
        img.setAttribute('src','/metadata/images/arrow-down.png')
        menu_bar_item.setAttribute('OnClick', 'Tree_Menu_MoveDown(id)');
        menu_bar_item.setAttribute('title', 'Move object DOWN');
    }
    if (CommandName === 'Refresh') {
        img.setAttribute('src','/metadata/images/refresh.png')
        menu_bar_item.setAttribute('OnClick', 'Tree_Menu_Refresh(id)');
        menu_bar_item.setAttribute('title', 'Refresh tree');
    }
    if (CommandName === 'Generate') {
        img.setAttribute('src','/metadata/images/ExternalData.png')
        menu_bar_item.setAttribute('OnClick', 'Generate(id)');
        menu_bar_item.setAttribute('title', 'Generate ORM module');
    }
    
    img.setAttribute('width','16px')
    img.setAttribute('height','16px')
    menu_bar_item.appendChild(img);
    if (ShowTitle) {
        lab = document.createElement('a');
        lab.innerHTML = CommandName
        menu_bar_item.appendChild(lab);
    }    
    
    
    parentContainer.appendChild(menu_bar_item);

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
    
    
    drawMenuButton(menu_bar,'Create', false);
    drawMenuButton(menu_bar,'Delete', false);
    drawMenuButton(menu_bar,'MoveUp', false);
    drawMenuButton(menu_bar,'MoveDown', false);
    drawMenuButton(menu_bar,'Refresh', false);
    drawMenuButton(menu_bar,'Generate', false);


    container.appendChild(menu_bar);

    tree_container = document.createElement('div');
    tree_container.className = 'tree-body'
    container.appendChild(tree_container);


    //ELEMENTS

    root_el = document.createElement('div');
    root_el.setAttribute('name', 'TreeID.root');
    root_el.innerHTML = '<a>root</a>';
   
    let MetadataTypes = ["Catalogs" , "Documents", "InformationRegisters"];

    let nextID = myTree.getNextID();

    for (MetadataType of MetadataTypes) {
        FullName0 = TreeID + '.'+MetadataType;
        
        MetadataTypeElem = DrawFirstLevelElement(tree_container, MetadataType, MetadataType, 1, FullName0);
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

    FinishedTypes = ["Attributes", "Forms","Commands", "Templates", "Dimentions", "Resourses"]
    if (FinishedTypes.includes(ItemType)){
    //if (SubItemsCount === '-1') {
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
    span.setAttribute('parent_id', rootElement.id);

    root_catalog4.setAttribute('id', nextID + '.root')
    
    root_catalog4.appendChild(span);

    root_catalog.appendChild(root_catalog4)
 
    rootElement.appendChild(root_catalog)

    return root_catalog4;

/*




*/
}

function DrawCatalogItemElement(nextID, rootElement, item, Name, Title, levelNumber)  {
    DrawFirstLevelElement(nextID, rootElement, 'Catalogs', item.Name, levelNumber)  
}

function CreateItem(path, ParentID){
    
    console.log(path)
    
    let FieldName = path[0]      //1
    let MetadataType = path[1]   //2 - Catalogs, Documents, InformationRegisters
    let MetadataName = path[2]   //3  name of previous objects
    let SubType1 = path[3]       //4  Attributes, TabularSections, Forms, Commands, Templates
    let SubType2 = path[4]       //5  name of previous objects
    let SubType3 = path[5]       //6  name of Attributes of tabular sections
    let SubType4 = path[6]       //7  

    
    let newItemStructure = {
       // FieldName : FieldName,
        Action : 'new',
        Name :  '',
        Path : path.join('.'),
        Result : false
    }

    adr = '' + SITE_ADRESS  + '' + MetadataType;
    for (let i=2; i<=6; i++){
        if (path[i] != undefined) {
            ard = adr + '/' +  path[i]}
        else {
            break
        }    
    }

    adr = '' + SITE_ADRESS  + 'CreateItem';
    
    if (adr ==='') {
        // ClearProperty()
     }
     else {
         console.log('save property:')
         console.log(adr)
         console.log(newItemStructure)
         
         takeDateFromSite_Fetch(adr, Method='PUT', Action='NewItem', Component = ParentID, newItemStructure)
     }  

    //let ss = '.'.join(path)
    //console.log(ss)

}

function Tree_Menu_Create(id) {
    
    let CurrentID = mytree1.selectedItem;
    let myOb = document.getElementById(CurrentID);
    let ParentID =myOb.getAttribute('parent_id');
    

    let FieldName = myOb.getAttribute('id0')      //1
    let MetadataType = myOb.getAttribute('id1')   //2 - Catalogs, Documents, InformationRegisters
    let MetadataName = myOb.getAttribute('id2')   //3  name of previous objects
    let SubType1 = myOb.getAttribute('id3')       //4  Attributes, TabularSections, Forms, Commands, Templates
    let SubType2 = myOb.getAttribute('id4')       //5  name of previous objects
    let SubType3 = myOb.getAttribute('id5')       //6  name of Attributes of tabular sections
    let SubType4 = myOb.getAttribute('id6')       //7  item - tabulat sec attribute

    let id_count = myOb.getAttribute('id_count')       //7  

    if (id_count =='7'){  //attrib of tab section
        //alert('Create attribute for ' + MetadataName + " tab " + SubType2 + '  ' + SubType3);
        CreateItem([FieldName,MetadataType,MetadataName, SubType1, SubType2,SubType3], ParentID);
    }    
    
    if (id_count =='6'){
        if (SubType2 === 'TabularSections'){
            //alert('Create attribute for ' + MetadataName + " tab " + SubType3);
            CreateItem([FieldName,MetadataType,MetadataName, SubType1, SubType2,SubType3], ParentID);
        }
        else {
            CreateItem([FieldName,MetadataType,MetadataName, SubType1, SubType2,SubType3], ParentID);
        }
    }        
        
    if (id_count == '5'){
        if (SubType2 === 'TabularSections'){
            //alert('Create tabular section for ' + MetadataName);
            CreateItem([FieldName,MetadataType,MetadataName, SubType1, SubType2,SubType3], ParentID);
        }
        else{
            //alert('Create 4 new  ' + SubType1);
            CreateItem([FieldName,MetadataType,MetadataName, SubType1], ParentID);

        }    
    }    

    if (id_count == '4'){
        CreateItem([FieldName,MetadataType,MetadataName, SubType1], CurrentID);
        //    alert('Create 4 new  ' + SubType1);
    }    
    
    if (id_count == '3'){
        //alert('Create new  ' + MetadataType);
        CreateItem([FieldName,MetadataType], ParentID);

    }
    
    if (id_count == '2'){
        CreateItem([FieldName,MetadataType], CurrentID, CurrentID);

    }    
    

}

function Tree_Menu_Create_Action(res, headers){

    if (res.Result) {
        
        let words = res.Path.split('.')
        let SubGroup = words[words.length-1]
        console.log(SubGroup); 

        let parent_ob = document.getElementById(headers.Component);
        
        SubItemName = res.Name;
        FullName3 = res.Path + '.' + SubItemName;
        DrawFirstLevelElement(parent_ob, SubItemName, SubItemName, 0, FullName3,"0" , SubGroup);



        //newItem = document.createElement('div');
        //newItem.innerHTML = res.Name;
        //parent_ob.appendChild(newItem);
    }
}

function Tree_Menu_Delete(id) {
    let CurrentID = mytree1.selectedItem;
    let myOb = document.getElementById(CurrentID);
    let ParentID =myOb.getAttribute('parent_id');
    

    let FieldName = myOb.getAttribute('id0')      //1
    let MetadataType = myOb.getAttribute('id1')   //2 - Catalogs, Documents, InformationRegisters
    let MetadataName = myOb.getAttribute('id2')   //3  name of previous objects
    let SubType1 = myOb.getAttribute('id3')       //4  Attributes, TabularSections, Forms, Commands, Templates
    let SubType2 = myOb.getAttribute('id4')       //5  name of previous objects
    let SubType3 = myOb.getAttribute('id5')       //6  name of Attributes of tabular sections
    let SubType4 = myOb.getAttribute('id6')       //7  item - tabulat sec attribute

    let id_count = myOb.getAttribute('id_count')       //7  

    if (id_count =='7'){  //attrib of tab section
        //alert('Create attribute for ' + MetadataName + " tab " + SubType2 + '  ' + SubType3);

        DeleteItem([MetadataType,MetadataName, SubType1, SubType2,SubType3,SubType4], CurrentID, ParentID);
    }    
        
    if (id_count == '5'){
        if (SubType2 === 'TabularSections'){
            //alert('Create tabular section for ' + MetadataName);
            DeleteItem([MetadataType,MetadataName, SubType1, SubType2,SubType3], CurrentID, ParentID);
        }
        else{
            //alert('Create 4 new  ' + SubType1);
            DeleteItem([MetadataType,MetadataName, SubType1,SubType2], CurrentID, ParentID);

        }    
    }    

     
    if (id_count == '3'){
        //alert('Create new  ' + MetadataType);
        DeleteItem([MetadataType, MetadataName], CurrentID, ParentID);

    }
    
}

function DeleteItem(Path, CurrentID, ParentID){
    console.log('Delete path')
    console.log(Path)

    adr = '' + SITE_ADRESS  + '' + Path.join('/');
    newItemStructure = {}
    
    if (adr ==='') {
        // ClearProperty()
     }
     else {
         console.log('Delete property:')
         console.log(adr)
         
         takeDateFromSite_Fetch(adr, Method='DELETE', Action='DeleteItem', Component = CurrentID, newItemStructure)
     }  

}
function Tree_Menu_Delete_Action(res, headers){

    console.log('Request result:')
    console.log(res);


}    

function Tree_Menu_MoveUp(id) {
    alert('move up');
}

function Tree_Menu_MoveDown(id) {
    alert('move down');
}

function Tree_Menu_Refresh(id) {
    alert('Refresh');
}