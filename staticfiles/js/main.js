 // Get search form and page links
 let searchForm = document.getElementById('searchForm');
 let pageLinks = document.getElementsByClassName('page-link');

 // Ensure search form exists
 if (searchForm) {
     for (let i = 0; i < pageLinks.length; i++) {
         pageLinks[i].addEventListener('click', function(e) {
             e.preventDefault();
             // Get data attribute
             let page = this.dataset.page;
             console.log('page:', page);

             // Add hidden search input to the form
             let hiddenInput = document.createElement('input');
             hiddenInput.type = 'hidden';
             hiddenInput.value = page;
             hiddenInput.name = 'page';
             searchForm.appendChild(hiddenInput);

             // Submit the form
             searchForm.submit();
         });
     }
 }


 //remove tag

 let tags = document.getElementsByClassName('project-tag')

 for(let i=0; i<tags.length; i++ ){
     tags[i].addEventListener('click', (e)=>{
         let tagID = e.target.dataset.tag
         let projectID = e.target.dataset.project

         //console.log('PROJECTID: ',projectID)
         //console.log('TAGID: ', tagID)
         fetch('http://127.0.0.1:8000/api/remove-tag/', {
             method: 'DELETE',
             headers: {
                 'Content-Type': 'application/json'
             },
             body: JSON.stringify({ 'project': projectID, 'tag': tagID }) // Proper object syntax
         })
         .then(response => response.json())
         .then(data => {
             e.target.remove();
         })
         .catch(error => {
             console.error('Error:', error);
         });
         
     })
 }