$(document).ready(function(){
    
    $(".f1").show();
    $(".f2").hide();
    $(".f3").hide();
    $(".fe").hide();
    document.getElementById("f2logo").style.borderColor = "#000";
    document.getElementById("f3logo").style.borderColor = "#000";
    document.getElementById("felogo").style.borderColor = "#000";
    document.getElementById("f1logo").style.borderColor = "#ee0000";

    $("#f1logo").click(function(){
        $(".f1").show();
        $(".f2").hide();
        $(".f3").hide();
        $(".fe").hide();
        document.getElementById("f2logo").style.borderColor = "#000";
        document.getElementById("f3logo").style.borderColor = "#000";
        document.getElementById("felogo").style.borderColor = "#000";
        document.getElementById("f1logo").style.borderColor = "#ee0000";
    });

    $("#f2logo").click(function(){
        $(".f1").hide();
        $(".f2").show();
        $(".f3").hide();
        $(".fe").hide();
        document.getElementById("f1logo").style.borderColor = "#000";
        document.getElementById("f3logo").style.borderColor = "#000";
        document.getElementById("felogo").style.borderColor = "#000";
        document.getElementById("f2logo").style.borderColor = "#0090d0";
      });

      $("#f3logo").click(function(){
        $(".f1").hide();
        $(".f2").hide();
        $(".f3").show();
        $(".fe").hide();
        document.getElementById("f1logo").style.borderColor = "#000";
        document.getElementById("f2logo").style.borderColor = "#000";
        document.getElementById("felogo").style.borderColor = "#000";
        document.getElementById("f3logo").style.borderColor = "#e90300";
      });

      $("#felogo").click(function(){
        $(".f1").hide();
        $(".f2").hide();
        $(".f3").hide();
        $(".fe").show();
        document.getElementById("f1logo").style.borderColor = "#000";
        document.getElementById("f2logo").style.borderColor = "#000";
        document.getElementById("f3logo").style.borderColor = "#000";
        document.getElementById("felogo").style.borderColor = "#14b7ed";
      });
  });