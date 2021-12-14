function returnBook(bookId,bookISBN){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    headers ={
        'X-CSRFToken': csrftoken
    }   
    axios.post("return_book/",{ 'bookId': bookId},{'headers': headers}).then(response=>{
        if (response.data.message.includes("success")){
                let e = document.getElementById(bookISBN)
                e.parentElement.removeChild(e);
                books = document.getElementsByClassName('main-book')
                num = 0;
                counterClicks = books.length/2;
                counterClicks2 = 0;
        }

    }).catch (err=>{
        alert(err)
    })
}

function extend(bookId,bookISBN,extended){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    headers ={
        'X-CSRFToken': csrftoken
    }   
    axios.post("extend_book/",{ 'bookId': bookId},{'headers': headers}).then(response=>{
        if (response.data.message.includes("success")){
            document.getElementById("return_"+bookISBN).innerText = response.data.newDate
        }

    }).catch (err=>{
        alert(err)
    })
}