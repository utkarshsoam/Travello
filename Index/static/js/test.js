
function common(uid,id){

    for(var i=0;i<uid.length;i++)
    if(id==uid[i].getid())
    {
    window.location.href=uid[i].geturl()
  
    }
  
}

function redirect()
{
    console.log("hi")
   
    window.location.href="/accounts/login";
    alert("Login Required");
}
function redirecting()
{
    console.log("hi")
   
    window.location.href="/accounts/login";
    alert("Login Required");
}

function scrollDown()
    {
        console.log("hiu");
        //window.scrollBy(0,250)
    }

// $('#show').click(function()
// {
//     $('#show').css('display','none')

// });

// $('#scroll').on('load',function()
// {
//     console.log("ji");
//     window.scrollBy(0,250);
// },5000);