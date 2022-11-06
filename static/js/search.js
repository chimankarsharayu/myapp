const input = document.getElementById('search');
const result = document.getElementById('results');


const addHtmlToElement =(element,html)=> {
    element.innerHTML = html;
}

const  fetchResult = value =>{
    if(value){
        
        const url = `/fetch_data/${value}/`;
        fetch(url,{
            method:"GET"
        })
        .then(response => {
            return response.json();
        })
        .then(data=>{
            let html = ''
            for(let d of data){
                html+=`<li class="list-group-item" >${d.name}</li>`;
                // console.log(d.name)
            }
            addHtmlToElement(result,html)
            
        })
        .catch(err=>{
            console.log(err);
        })
    }else{
        addHtmlToElement(result,'')
    }
}

input.onkeyup = ()=>fetchResult(input.value)