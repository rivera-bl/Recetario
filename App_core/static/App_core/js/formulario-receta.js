function Events(){

    document.querySelector('#btn-añadir').addEventListener('click', AñadirIngrediente);
    let botonesEliminar = document.querySelectorAll('#btn-eliminar')

    for (let i = 0; i < botonesEliminar.length; i++) {
        
        botonesEliminar[i].addEventListener('click', EliminarIngrediente);
    }
}


function AñadirIngrediente(e){
    e.preventDefault();
    
    let listaIngredientes = document.querySelector('#lista-ingredientes');
    let ingrediente = document.querySelector('#input-ingredient').value;

    //Validacion input ingredientes
    if(ingrediente === ""){
        let form = document.querySelector('.form-nueva-receta');
        let error = form.children[2].children[1];

        let mensajeError = document.createElement('div');

        mensajeError.innerHTML = `        
            <p class="error-msg">La casilla de ingredientes no puede estar vacia</p>
        `;

        if(error.childElementCount < 1){
            error.appendChild(mensajeError);   
        }
    }

    //Si el input de ingredientes es valido
    else{

        //Eliminar mensaje de error previo
        let error = document.querySelector('#e-ingrediente');
        if(error.childElementCount){
            
            console.log(error);

            error.removeChild(error.children[0]);
        }
        
        //Añadir ingredientes
        let nuevoIngrediente = document.createElement('li');
        nuevoIngrediente.setAttribute("id", "id-ingredient");
    
        nuevoIngrediente.innerHTML = ` 
            
            <span>${ingrediente}</span>
            <button class="icon-borrar" type="button" id="btn-eliminar"><i class="fas fa-times"></i></button>       
        `;
    
        listaIngredientes.appendChild(nuevoIngrediente);
       
        document.querySelector('#input-ingredient').value = "";
    
        //Agregando evento a los nuevos ingredientes
        let botonesEliminar = document.querySelectorAll('#btn-eliminar')
    
        for (let i = 0; i < botonesEliminar.length; i++) {
            
            botonesEliminar[i].addEventListener('click', EliminarIngrediente);
        }
    }
    

}

function EliminarIngrediente(e){
    e.preventDefault();

    ingrediente = this.parentNode.parentNode

    ingrediente.removeChild(this.parentNode);
    
}

Events();