var express=require("express")
var app=express();
app.use(express.static("public"));
app.set("view engine","ejs");
app.set("views","./views");

var server=require("http").Server(app);
var io=require("socket.io")(server);
server.listen(process.env.PORT || 3000);

io.on("connection",function(socket){
  console.log("co nguoi ket noi");
  socket.on("disconnect",function(){
    console.log("ngat ket noi");
  });
});

app.get("/",function(req,res){
  res.render("a")
});
