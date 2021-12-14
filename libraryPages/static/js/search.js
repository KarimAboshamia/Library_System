
function searchFilter()
{
    input = document.createElement("input");
    input.setAttribute("type", "text");
    input.setAttribute("name", "value")
    document.getElementById("search").appendChild(input)
}

function getData()
{
    for (let i in Object.keys(ele))
    {
        console.log (i)
        break
    }
}