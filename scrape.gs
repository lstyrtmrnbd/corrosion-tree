// GOOGLE Sheets script
// scrape the data necessary for embedding in corrosion.py
function quickScrape() {
  
  Logger.log(scrapeMetalInfo(SpreadsheetApp.getActiveSheet(), "B"));
}

function fullScrape() {
 
  scrapeMetalInfos(10);
}

function scrapeMetalInfo(spreadsheet, columnString) {
  
  var valueRange = "Sheet1!" + columnString + "5:" + columnString + "11";
  //Logger.log("Value query: " + valueRange);
  
  var labels = spreadsheet.getRange("Sheet1!A6:A11").getValues();
  var values = spreadsheet.getRange(valueRange).getValues();
  
  return formatRawInfo(labels, values);
}

// scrapes and concats all info
function scrapeMetalInfos(count) {
  
  var ss = SpreadsheetApp.getActiveSheet();
  var infos = "";
  
  var colLetter = "";
  for(var i = 0; i < count; i++) {
   
    colLetter = String.fromCharCode(66 + i); // 66 is 'B'
    //Logger.log(colLetter);
    infos += scrapeMetalInfo(ss, colLetter) + ",\n\n";
  }
  
  Logger.log(infos);
}

function formatRawInfo(labels, values) {

  var formattedString = "MetalInfo({\n" + 
                        "    \"name\":\"" + values[0] + "\",\n" + 
                        "    \"picture\":\"\",\n";
  
  for(var i = 0; i < labels.length; i++) {
    
    var label = labels[i][0].split("(");
    label = label[0].trim();
    
    formattedString += "    ";
    formattedString += "\"" + label + "\":\"" + values[i + 1] + "\",\n";
  }
  
  formattedString += "})"
  
  return formattedString; // returns a MetalInfo def
}
