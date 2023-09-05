
class PropertyWin{
    
    constructor (id){
        this.id = id;
        this.object_name = "";
        this.prop_id_list = [];

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


        new_input = document.createElement('input');
        if (FieldStruct['Type'] === 'String'){
            new_input.setAttribute('type', 'text')
        }
        else if (FieldStruct['Type'] === 'Boolean'){
            new_input.setAttribute('type', 'checkbox')
        } 
        else if (FieldStruct['Type'] === 'Integer'){
            new_input.setAttribute('type', 'number')
        }
        else {
            new_input.setAttribute('type', 'text')
        }

        if (PropertyName in Struct[PROP_VALUE]) {
            if ('Value' in Struct[PROP_VALUE][PropertyName]) {
                let TempValue = Struct[PROP_VALUE][PropertyName][PROP_VALUE]
                if (TempValue === undefined) {}
                else
                {
                    new_input.setAttribute('value', TempValue)
                }
            }
        }

        new_input.addEventListener("change", updateValue);
        new_input.setAttribute('id', id_input)
        new_input.setAttribute('PropertyName', PropertyName)
        new_input.setAttribute('Name', PropertyName)

        new_td = document.createElement('td');
        new_td.className = 'value-column';
        
        new_td.appendChild(new_input)
        new_tr.appendChild(new_td)
       
        container.appendChild(new_tr);

        Obj.prop_id_list.push(id);

    }
     
    
    //new_label.no

}

function updateValue(e) {
    //
    //sent new value to server
    //

    log2 = document.getElementById('ss')
    log2.innerHTML = e.target.value;

    
    let words = myProp.object_name.split('.')
    
    let FieldName = words[0]      //1
    let MetadataType = words[1]   //2 - Catalogs, Documents, InformationRegisters
    let MetadataName = words[2]   //3  name of previous objects
    let SubType1 = words[3]       //4  Attributes, TabularSections, Forms, Commands, Templates
    let SubType2 = words[4]       //5  name of previous objects
    let SubType3 = words[5]       //6  name of Attributes of tabular sections
    let SubType4 = words[6]       //7  

    let PropName = e.srcElement.id  //"property.input.Comment"
    let words2 = PropName.split('.')
    PropName = words2[2]



    let newValue = {
        "Name" : "sdsdsd",
        "Value" :  "" + e.target.value,
        "Path"  : "" + myProp.object_name,  //"mytree1.Catalogs.Goods"
        'PropName' : PropName ,
        "res" : ''  
        }



    let adr = ''

    if (words.length === 3) {
        adr = '' + SITE_ADRESS  + '' + MetadataType + '/' + MetadataName + '/Property/' + PropName;
    }
    else if (words.length === 5) {
        adr = '' + SITE_ADRESS  + '' + MetadataType + '/' + MetadataName + '/' + SubType1 + '/' + PropName;
        if (SubType1 === 'TabularSections') {
            adr = '' + SITE_ADRESS  + '' + MetadataType + '/' + MetadataName + '/' + SubType1 + '/Properties/' + PropName;
        }
    }    
    else if (words.length === 7) {
        adr = '' + SITE_ADRESS  + '' + MetadataType + '/' + MetadataName + '/' + SubType1 + '/' + SubType2 + '/' + SubType3 + '/' +SubType4;
    }    
   
    if (adr ==='') {
       // ClearProperty()
    }
    else {
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



