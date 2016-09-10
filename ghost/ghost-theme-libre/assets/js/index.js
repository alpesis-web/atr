/*global
	$
*/
$(document).ready(function () {

	'use strict';

	var $grid = $('.grid'),
		$textItems = $grid.find('.grid-item');

	$grid = $('.grid').masonry({
        itemSelector: '.grid-item'
    });

    $grid.imagesLoaded().progress(function (imgLoad, image) {
        var $gridItem = $(image.img).parents('.grid-item');
        $gridItem.fadeIn('fast').removeClass('loading');
        if (image.isLoaded) {
            $gridItem.addClass('loaded');
        } else {
            $gridItem.addClass('unloaded');
        }
        $grid.masonry('layout');
    });
});
