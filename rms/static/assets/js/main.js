
/* modal window shering page 6 */






const modalShering = () => {
  let listButtonElem = $('.main__container-button2');
  let modalCategoryElem = $('.modal-shering');
  let sheringInput = $('.shering_input');

  modalCategoryElem.css({
    'display': 'flex',
    'visibility': 'hidden',
    'opacity': '0',
    'transition': 'opacity 300ms ease-in-out'
  });

  const closeModal = event => {
    const target = $(event.target);

    if (target.is(modalCategoryElem) || target.closest('.modal-category_button1').length > 0) {
      modalCategoryElem.css('opacity', '0');

      setTimeout(() => {
        modalCategoryElem.css('visibility', 'hidden');
      }, 300);

      $(window).off('keydown', closeModal);
    }
  }

  let openModal = () => {
    modalCategoryElem.css({
      'visibility': 'visible',
      'opacity': '1'
    });
  };

  modalCategoryElem.on('click', closeModal);

  listButtonElem.on('click', openModal);


  modalCategoryElem.on('click', '.shering-frame', () => {
    sheringInput.select();
    document.execCommand('copy');
    closeModal(); 

  });
};

modalShering();







/* search page 4 */

$(document).ready(function() {
 
  var tableRows = $('.first tr');
  var searchInput = $('.search-txt');

  
  searchInput.on('keyup', function() {
    
    var searchText = $(this).val().toLowerCase();

    
    tableRows.each(function() {
      var rowText = $(this).text().toLowerCase();
      if (rowText.indexOf(searchText) === -1) {
        $(this).hide();
      } else {
        $(this).show();
      }
    });
  });
});






const modalDelete = () => {
  let listButtonElem = $('.main__container-button1');
  let modalCategoryElem = $('.modal-delete');

  modalCategoryElem.css({
    'display': 'flex',
    'visibility': 'hidden',
    'opacity': '0',
    'transition': 'opacity 300ms ease-in-out'
  });

  const closeModal = event => {
    const target = $(event.target);

    if (target.is(modalCategoryElem) || target.closest('.modal-category_button1, .modal-delete_button2').length > 0) {
      modalCategoryElem.css('opacity', '0');

      setTimeout(() => {
        modalCategoryElem.css('visibility', 'hidden');
      }, 300);

      $(window).off('keydown', closeModal);
    }
  }

  let openModal = () => {
    modalCategoryElem.css({
      'visibility': 'visible',
      'opacity': '1'
    });
  };

  modalCategoryElem.on('click', closeModal);

  listButtonElem.on('click', openModal);
};

modalDelete();







/*const tr = document.querySelector('tr');
tr.addEventListener('click', () => {
  location.href = "";
});*/




  




