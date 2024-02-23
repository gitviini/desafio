const desafios = document.querySelector("#desafios")
const menu = document.querySelector('#menu')
const menu_label = document.querySelector(".menu_label")
const container_content = document.querySelector('#container_content')
const container_topic = document.querySelector('#container_topic')
const path = '/center/'

let topic_select = ''

get_list(topic_select)

desafios.onclick = () =>{
    desafios.classList.toggle('show')
    menu.classList.toggle('show')
    if (menu.classList.value){
        document.onclick = (event) =>{
            if (event.x > 450){
                menu.classList.remove('show')
            }
        }
    }
}

async function get_list(topic_select=''){
    const resp = await fetch(path,{
        method:'POST',
        headers:{
            'Content-Type':'application/json; mode=get_content',
        },
        body:JSON.stringify({'topic':topic_select})
    })
    const data = await resp.json()
    if(topic_select == ''){
        topic_select = data['topic'][0][0]
    }

    console.log(data)

    gerenate(data, topic_select)
}

function gerenate(data=[], topic_select=''){
    menu_label.innerHTML = topic_select
    let topic_content = data[topic_select]
    let topic_option = data['topic']

    container_topic.innerHTML =''
    container_content.innerHTML =''

    for(let n = 0; n < topic_option.length; n++){
        let topic = document.createElement('li')
        topic.setAttribute('class','topic')
        topic.setAttribute('value',topic_option[n][0])
        let topic_img = document.createElement('img')
        topic_img.src = topic_option[n][1]
        topic_img.alt = topic_option[n][0]
        topic.appendChild(topic_img)
        topic.onclick = () =>{
            topic_select = topic.getAttribute('value')
            get_list(topic_select)
        }
        container_topic.appendChild(topic)
    }

    topic_content.forEach(quest=>{
        let li = document.createElement('li')
        let a = document.createElement('a')
        a.setAttribute('class','content')
        a.href = `/${topic_select}/${quest[0]}`
        a.innerText = quest[0]
        li.appendChild(a)
        container_content.appendChild(li)
    })
}