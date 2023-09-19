
class PropertyWin{
    
    constructor (id){
        this.id = id;
        this.object_name = "";
        this.prop_id_list = [];

        
        this.currentPropID = "";
        
        this.firstValue = "";
        this.firstValueAsNumber = 0;
        this.firstValueAsBoolean = false;

    }
}


function ShowProperty(Obj, Struct, Headers) {
    ClearProperty();
    myProp.object_name = Obj.id

    let container = document.getElementById('property');

   // Obj.prop_id_list.push('prop1');

    for (PropertyName in Struct.PropertyList){
        let FieldStruct = Struct.PropertyList[PropertyName]
        //console.log(item)
        id = 'property.' + PropertyName;
        id_input = 'property.input.' + PropertyName;

        new_tr = document.createElement('tr');
        new_tr.setAttribute('height','5px')
        new_tr.setAttribute('id', id);

        new_td = document.createElement('td');
        new_td.innerHTML = PropertyName
        new_tr.appendChild(new_td)

        
        if (FieldStruct.Selectable === true) {
            new_input = document.createElement('select');
            new_input.setAttribute('width', "100%")

            for (option_item of FieldStruct.SelectList){
                new_option = document.createElement('option');
                new_option.value = option_item
                new_option.innerHTML = option_item

                new_input.appendChild(new_option)
            }    

        }
        else {
            new_input = document.createElement('input');
        }

        new_input.addEventListener("change", updateValue);
        
        new_input.setAttribute('onfocusin', 'onfocusProperty(this)');
        new_input.setAttribute('onfocusout', 'onfocusOutProperty(this)');
        
        new_input.setAttribute('id', id_input)
        new_input.setAttribute('PropertyName', PropertyName)
        new_input.setAttribute('Name', PropertyName)
        new_input.className = 'enterfield'

        if (PropertyName === 'Name') {
            new_input.setAttribute('pattern', '[a-zA-Z]')
            new_input.setAttribute('Title', 'Identifier rules')
        }

        let TempValue = undefined;

        if (PropertyName in Struct[PROP_VALUE]) {
            if ('Value' in Struct[PROP_VALUE][PropertyName]) {
                TempValue = Struct[PROP_VALUE][PropertyName][PROP_VALUE]
            }
            if (Struct[PROP_VALUE][PropertyName]['Edidable'] == true ) {


            }


        }

        if (FieldStruct['Type'] === 'String'){
            new_input.type = 'text'
            
            if (TempValue != undefined) {
                new_input.value = TempValue
            }
        }
        else if (FieldStruct['Type'] === 'Boolean'){
            new_input.type = 'checkbox'
            if (TempValue != undefined) {
                new_input.checked = TempValue
            }
        } 
        else if (FieldStruct['Type'] === 'Integer'){
            new_input.type = 'number'
            //new_input.setAttribute('align', 'right')
            new_input.className = 'input_number'
            
            if (TempValue != undefined) {
                new_input.valueAsNumber = TempValue
            }
        }
        else {
            new_input.type = 'text'
            if (TempValue != undefined) {
                new_input.value = TempValue
            }
        }

        

        
        new_td = document.createElement('td');
        new_td.className = 'value-column';
        
        new_td.appendChild(new_input)
        new_tr.appendChild(new_td)
       
        container.appendChild(new_tr);

        Obj.prop_id_list.push(id);

    }
     
    
    //new_label.no

}

function onfocusProperty(ff) {

    ob = document.getElementById('prop_label')
    ob.innerHTML = '' + ff.value + '  ' + ff.id;
    myProp.currentPropID = ff.id;
    myProp.firstValue = ff.value;
    myProp.firstValueAsNumber = ff.ValueAsNumber;
    myProp.firstValueAsBoolean = ff.ValueAsBool;
    
    //alert('dfdf')
}

function onfocusOutProperty(ff) {

    ob.innerHTML = '';
    myProp.currentPropID = '';
  
    myProp.firstValue = '';
    myProp.firstValueAsNumber = 0;
    myProp.firstValueAsBoolean = false;
  
}



function updateValue(e) {
    //
    //sent new value to server
    //
    
    let PropName  = e.srcElement.id  //"property.input.Comment"
    let words2 = PropName.split('.')
    PropName = words2[2]
    
    let newValue2 = e.target.value
    if (e.target.type === 'checkbox') {
        if (e.target.checked) {
            newValue2 = 'True'
            newValue2 = true
            //newValue2 = 1
        } else {
            newValue2 = 'False'
            newValue2 = false
            //newValue2 = 0
        }
    }
    
    if (e.target.type === 'number') {
        newValue2 = e.target.valueAsNumber
    }
    
    log2 = document.getElementById('ss')
    log2.innerHTML = newValue2;

    
    //let words = myProp.object_name.split('.')
    let myOb = document.getElementById(myProp.object_name);
  
    let FieldName = myOb.getAttribute('id0')      //1
    let MetadataType = myOb.getAttribute('id1')   //2 - Catalogs, Documents, InformationRegisters
    let MetadataName = myOb.getAttribute('id2')   //3  name of previous objects
    let SubType1 = myOb.getAttribute('id3')       //4  Attributes, TabularSections, Forms, Commands, Templates
    let SubType2 = myOb.getAttribute('id4')       //5  name of previous objects
    let SubType3 = myOb.getAttribute('id5')       //6  name of Attributes of tabular sections
    let SubType4 = myOb.getAttribute('id6')       //7  

    let id_count = myOb.getAttribute('id_count')       //7  
  


    let newValue = {
        //"Name" : "sdsdsd",
        "Value" :  '' + newValue2,
        "ValueType" :  e.target.type,
        "ValueAsBool" :  false,
        "ValueAsNumber" :  0,
        
        //"PropertyPath"  : "" + myProp.object_name,  //"mytree1.Catalogs.Goods"
        'PropertyName' : PropName ,
        //'new_id' : '',
        "res" : ''  
        }

    if (e.target.type === 'checkbox') {    
        newValue.ValueAsBool = newValue2 
    }    
    if (e.target.type === 'number') {    
        newValue.ValueAsNumber = newValue2 
    }    

    let adr = ''

    let new_id = myProp.object_name.split('.')

    if (id_count == 3) {
        adr = '' + SITE_ADRESS  + '' + MetadataType + '/' + MetadataName + '/Properties/' + PropName;
    }
    else if (id_count == 5) {
        adr = '' + SITE_ADRESS  + '' + MetadataType + '/' + MetadataName + '/' + SubType1 + '/' + SubType2;

        if (SubType1 === 'TabularSections') {
            adr = adr + '/Properties/' + PropName;
        }
        
    }    
    else if (id_count == 7) {
        adr = '' + SITE_ADRESS  + '' + MetadataType + '/' + MetadataName + '/' + SubType1 + '/' + SubType2 + '/' + SubType3 + '/' +SubType4;
    }    
   
    //if (PropName === 'Name') {
    //    new_id[myLevel-1] = '' + newValue2
    //}

    //new_id = new_id.join('.');
    //newValue.new_id = new_id;

    if (adr ==='') {
       // ClearProperty()
    }
    else {
        console.log('save property:')
        console.log(adr)
        console.log(newValue)
        
        takeDateFromSite_Fetch(adr, Method='POST', Action='SaveNewValue', Component='property', newValue)
    }    



}


function ClearProperty(){
    container = document.getElementById('property');
 
   while (myProp.prop_id_list.length >0) {
        id = myProp.prop_id_list.pop()
        PropItem = document.getElementById(id);
        container.removeChild(PropItem);
    }
    
}



