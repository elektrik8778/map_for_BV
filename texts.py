

element_1 = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <div style="position: fixed; 
         top: 50px; left: 70px; width: 150px; height: 70px; 
         background-color:orange; border:2px solid grey;z-index: 900;">
         <button class="btn btn-primary" type="submit">Button1</button>
         <button class="btn btn-primary" type="submit">Button2</button>
         <button class="btn btn-primary" type="submit">Button3</button>
    </div>
    """

element_alt = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    
    <form class="row gy-2 gx-3 align-items-center">
    <div class="col-auto", style="position: fixed; 
         top: 50px; left: 70px;  
         background-color:orange; border:2px solid grey;z-index: 900;">
         <div class="col-auto">
            <label class="sr-only" for="autoSizingInput>Высота над уровнем моря (м)</label>
         </div>
         <div class="col-auto">
            <label class="sr-only" for="autoSizingInput">Name</label>
            <input type="text" class="form-control" id="autoSizingInput" placeholder="Jane Doe">
        </div>
         
         <button class="btn btn-primary" type="submit">Button1</button>
    </div>
    </form>
    """