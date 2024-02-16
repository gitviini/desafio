const calculator = document.querySelector("#calculator")
const numbers = document.querySelectorAll('.number')
const operations = document.querySelectorAll('#container_operation button')
const before = document.querySelector('#before')
const real = document.querySelector('#real')
const equal = document.querySelector('#equal')
const clear = document.querySelector('#clear')

class Calculator{
    constructor(equal=Node, clear=Node, display_real=Node, display_before=Node){
        this.mode_operation = ''
        this.a = 0
        this.b = 0
        this.equal = equal
        this.clear = clear
        this.displays = [display_real, display_before]
        this.real = '0'
        this.before = ''

        this.equal.onclick = () => this.do_operations(this.mode_operation, this.a, this.b)
        this.clear.onclick = () => this.clear_display()
    }

    show(){
        //update screen's data
        this.displays[0].innerHTML = this.real
        this.displays[1].innerHTML = this.before
    }

    clear_display(){
        this.real = '0'
        this.before = ''
        this.show()
    }

    up(){
        if (Number(this.real)){
            this.before = `${this.real} ${this.mode_operation}`
            this.b = Number(this.real)
        }
        else{
            this.before = `${this.b} ${this.mode_operation}`
        }
        this.real = '0'
        this.show()
    }

    do_operations(mode='', a=0, b=0){
        let result = 0
        switch (mode){
            case '+':
                result = b+a
                break
            case '-':
                result = b-a
                break
            case '/':
                result = b/a
                break
            case '*':
                result = b*a
                break
        }
        this.real = result
        this.before = ''
        this.show()
    }

    input(numA='',numB=''){
        if(this.real == '0'){
            this.real = numA
            this.a = Number(this.real)
        }
        else{
            this.real += numA
            this.a = Number(this.real)
        }

        this.show()
    }
}

const calc = new Calculator(equal, clear, real, before)

operations.forEach(operation =>{
    operation.onclick = () =>{
        calc.mode_operation = operation.value
        calc.up()
    }
})

numbers.forEach(number =>{
    number.onclick = () =>{
        calc.input(number.textContent)
    }
})

calculator.onsubmit = (event)=>{
    event.preventDefault()
}