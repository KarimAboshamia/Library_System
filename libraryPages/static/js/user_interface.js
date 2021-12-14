function borrowBook( bookID,bookISBN) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let copies = parseInt(document.getElementById(bookISBN+"_counter").innerText)
    headers ={
        'X-CSRFToken': csrftoken
    }   
    axios.post("borrow_book/",{ 'bookId': bookID},{'headers': headers}).then(response=>{
        alert(response.data.message)
        if (response.data.message.includes("borrowed successfully")){
            // if (c)
            copies  -= 1
            document.getElementById(bookISBN+"_counter").innerText = copies
            if (copies == 0){
                let e = document.getElementById(bookISBN)
                e.parentElement.removeChild(e);
                books = document.getElementsByClassName('main-book')
                num = 0;
                counterClicks = books.length/2;
                counterClicks2 = 0;
                // counter
            }

        }

    }).catch (err=>{
        alert(err)
    })
}