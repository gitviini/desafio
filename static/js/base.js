const desafios = document.querySelector("#desafios")

const path = '/center'

get_list().then(data=>{
    gerenate(data)
})

desafios.addEventListener('click',()=>{
    desafios.classList.toggle('show')
    document.querySelector('#container_menu').classList.toggle('show')
})

async function get_list(){
    const resp = await fetch(path,{
        method:'GET',
        headers:{
            'Content-Type':'text/html; mode=get_list'
        }
    })
    const data = await resp.json()
    return data
}

function gerenate(list=[]){
    list.forEach(quest=>{
        let li = document.createElement('li')
        let a = document.createElement('a')
        a.setAttribute('class','content')
        a.href = `/${quest}`
        a.innerText = quest
        li.appendChild(a)
        container_content.appendChild(li)
    })
}

const container_content = document.querySelector('#container_content')
const container_topic = document.querySelector('#container_topic')