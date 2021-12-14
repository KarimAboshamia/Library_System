var right_arrow = document.getElementById('left-arrow')
var left_arrow = document.getElementById('right-arrow')
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// console.log(books[0])
var books = document.getElementsByClassName('main-book')
let num = 0;
let counterClicks = books.length/2;
let counterClicks2 = 0;
right_arrow.addEventListener("click", function(){
    if(counterClicks > 0 ){
        num -= 500;
        counterClicks--;
        counterClicks2++;
    }
    for (var i = 0; i < books.length;i++){
        books[i].style.left = num.toString()+'px';
    }
})  

left_arrow.addEventListener("click", function(){
    if(counterClicks2>0){
        num += 500;
        counterClicks2--;
        counterClicks++;
    }
   for (var i = 0; i < books.length;i++){
        books[i].style.left = num.toString()+'px';
    }
})  



///----------- Jquery ----------
$(document).ready(function(){
    $(".filter-submit").click(function(){
        $.ajax({
            url: '../home',
            type: 'get',
            data: {
                type: $('#category').val(),
                author: $('#author').val(),
                ISBN: $('#ISBN').val(),
                publication_year: $('#publication_year').val(), 
            },
            success: function(response){
                data = response.books
                //console.log(data)
                viewedBooks = document.getElementsByClassName("main-book")
                let counter_3 =0
                for (i = 0; i < viewedBooks.length; i++)
                {
                    console.log(viewedBooks[i].id)
                    let exist= false
                    for (k = 0; k < data.length; k++)
                    {
                        if(data[k].ISBN == viewedBooks[i].id)
                        {
                            exist=true
                            break;
                        }
                    }
                    if(exist==true)
                    {
                        viewedBooks[i].style.display= 'block'
                        counter_3++
                    }
                    else
                    {
                        viewedBooks[i].style.display= 'none'
                    }    
                }
                counterClicks=counter_3/2
            }
        });
    });
});

