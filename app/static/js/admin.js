const form = document.querySelector('#container_form form')
const container_main = document.querySelector('#container_main')
const container_resp = document.querySelector('#container_resp')
console.log()

function get_cookie(mode=0){
    let cookies = document.cookie
    if (cookies.indexOf(';') != -1){
        cookies = cookies.split(';')
    }else{
        cookies = cookies.split('=')
    }

    return cookies[cookies.indexOf('csrftoken')+1]
}

async function generate_page(data=''){
    container_resp.innerHTML += data
}

async function get_admin_file(data={},function_generate=''){
    let info = {
        method:'POST',
        headers:{
            'Content-Type':'application/json; mode=admin_signed',
            'X-CSRFToken':get_cookie(),
        },
        body:JSON.stringify(data),
    }
    const req = await fetch('/admin',info)

    const resp = await req.json()
    function_generate(resp['resp'])
}

form.onsubmit = (event)=>{
    event.preventDefault()
    
    username = document.querySelector('#container_form form input[name="username"]').value
    password = document.querySelector('#container_form form input[name="password"]').value
    data = {
        'username':username,
        'password':password,
    }
    get_admin_file(data,generate_page)
}