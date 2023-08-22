




/* pop up  on button save thing page five */


/*const modalController = () => {
  const buttonElem = $('.button_send');
  const modalElem = $('.modal');

  modalElem.css({
    display: 'flex',
    visibility: 'hidden',
    opacity: 0,
    transition: 'opacity 300ms ease-in-out',
  });

  const closeModal = event => {
    const target = event.target;

    if (target === modalElem[0] || $(target).closest('.modal_close-button').length) {
      modalElem.css({ opacity: 0 });

      setTimeout(() => {
        modalElem.css({ visibility: 'hidden' });
      }, 300);

      $(window).off('keydown', closeModal);
    }
  };

  const openModal = () => {
    modalElem.css({ visibility: 'visible', opacity: 1 });
  };

  modalElem.on('click', closeModal);
  buttonElem.on('click', openModal);
};

modalController();*/




/* pop up make place page five */

const modalSaveController = () => {
  let listButtonElem = $('.button_send-delete');
  let modalCategoryElem = $('.modal-category');

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
};

modalSaveController();








/* modal window delete page 8 */



/*const modalDelete = () => {
  let listButtonElem = $('.button_send-delete');
  let modalCategoryElem = $('.modal-delete');

  modalCategoryElem.css({
    'display': 'flex',
    'visibility': 'hidden',
    'opacity': '0',
    'transition': 'opacity 300ms ease-in-out'
  });

  const closeModal = event => {
    const target = $(event.target);

    if (target.is(modalCategoryElem) || target.closest('.modal-category_button2').length > 0) {
      modalCategoryElem.css('opacity', '0');

      setTimeout(() => {
        modalCategoryElem.css('visibility', 'hidden');
      }, 300);

      $(window).off('keydown', closeModal);
    }
  };

  const closeModalFromButton = () => {
    modalCategoryElem.css('opacity', '0');

    setTimeout(() => {
      modalCategoryElem.css('visibility', 'hidden');
    }, 300);

    $(window).off('keydown', closeModal);
  };

  let openModal = () => {
    modalCategoryElem.css({
      'visibility': 'visible',
      'opacity': '1'
    });
  };

  modalCategoryElem.on('click', closeModal);

  listButtonElem.on('click', openModal);

  $('.modal-delete_button2').on('click', closeModalFromButton);
};

modalDelete()*/



