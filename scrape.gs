// Google Sheets script
// scrape the data necessary for embedding in corrosion.py
var indent = "    "

function quickScrape() {
  
  Logger.log(scrapeMetalInfo(SpreadsheetApp.getActiveSheet(), "B"));
}

function fullScrape() {
 
  scrapeMetalInfos(43);
}

function scrapeMetalInfo(spreadsheet, columnString) {
  
  var valueRange = "Sheet1!" + columnString + "5:" + columnString + "11";
  //Logger.log("Value query: " + valueRange);
  
  var labels = spreadsheet.getRange("Sheet1!A6:A11").getValues();
  var values = spreadsheet.getRange(valueRange).getValues();
  
  return formatXMLInfo(labels, values);
}

// scrapes count infos
function scrapeMetalInfos(count) {
  
  var ss = SpreadsheetApp.getActiveSheet();
  var infos = "";
  
  var colLetter = "";
  for(var i = 0; i < count; i++) {
   
    colLetter = countFromB(66 + i); // 66 is 'B'
    var value = scrapeMetalInfo(ss, colLetter);
    infos += value;
    //ss.getRange(colLetter + "14").setValue(value);
  }
  
  Logger.log(infos);
}

function countFromB(count) {
 
  var rem = 65;
  var colLetter = count;
  var column = String.fromCharCode(count);
  
  if(count > 90) {
   
   rem += count % 91;
   colLetter = 65;
   column = String.fromCharCode(colLetter) + String.fromCharCode(rem);
  }

  return column;
}

function formatXMLInfo(labels, values) {
 
  var formattedString = "<MetalInfo name=\"" + values[0] + "\" " + 
                        "picture=\"\" ";
  
  for(var i = 0; i < labels.length; i++) {
  
    var label = labels[i][0].split("(");
    label = label[0].trim();
  
    formattedString += label + "=\"" + values[i + 1] + "\" ";
  }
    
  formattedString += " />\n"
  
  return formattedString;
}

function formatRawInfo(labels, values) {

  var formattedString = "MetalInfo({\n" + 
                        indent + "\"name\":\"" + values[0] + "\",\n" + 
                        indent + "\"picture\":\"\",\n";
  
  for(var i = 0; i < labels.length; i++) {
    
    var label = labels[i][0].split("(");
    label = label[0].trim();
    
    formattedString += indent;
    formattedString += "\"" + label + "\":\"" + values[i + 1] + "\",\n";
  }
  
  formattedString += "})"
  
  return formattedString; // returns a MetalInfo def
}