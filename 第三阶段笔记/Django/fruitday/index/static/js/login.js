$(function(){
    $("#ab").submit(function{
        var uphone=$("name=uphone").val();
        var upwd=$("name=upwd").val();
        if (uphone.lenght==0 || upwd.lenght==0){
            return false;
        }return true;

    })
});