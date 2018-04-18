function fileChange(target,id) {
var fileSize = 0;
var filetypes =[".jpg",".png",".PNG",".jpeg",".gif",".JPEG"];
var filepath = target.value;
var filemaxsize = 1024*2;//2M
if(filepath){
var isnext = false;
var fileend = filepath.substring(filepath.indexOf("."));
if(filetypes && filetypes.length>0){
for(var i =0; i<filetypes.length;i++){
if(filetypes[i]==fileend){
isnext = true;
break;
}
}
}
if(!isnext){
alert("file type not supported!");
target.value ="";
return false;
}
}else{
return false;
}
if (isIE && !target.files) {
var filePath = target.value;
var fileSystem = new ActiveXObject("Scripting.FileSystemObject");
if(!fileSystem.FileExists(filePath)){
alert("please input again");
return false;
}
var file = fileSystem.GetFile (filePath);
fileSize = file.Size;
} else {
fileSize = target.files[0].size;
}

var size = fileSize / 1024;
if(size>filemaxsize){
alert("file size should not bigger than "+filemaxsize/1024+"M!");
target.value ="";
return false;
}
if(size<=0){
alert("file size should not be 0M!");
target.value ="";
return false;
}
}
