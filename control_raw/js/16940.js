function bindPopup (element, img) {
  // 图片点击时展现图片
  img.addEventListener('click', function (event) {
    event.stopPropagation()
    // 图片未加载则不弹层
    /* istanbul ignore if */
    if (img.width + img.naturalWidth === 0) {
      return
    }

    // Show page mask
    window.MIP.viewer.page.togglePageMask(true, {
      skipTransition: true,
      extraClass: 'black'
    })
    let popup = createPopup(element, img)
    let popupBg = popup.querySelector('.mip-img-popUp-bg')
    let mipCarousel = popup.querySelector('mip-carousel')
    let popupImg = new Image()
    popupImg.setAttribute('src', img.src)
    popup.appendChild(popupImg)

    let imgOffset = getImgOffset(img)

    popup.addEventListener('click', imagePop, false)

    function imagePop () {
      // Hide page mask
      window.MIP.viewer.page.togglePageMask(false, {
        skipTransition: true,
        extraClass: 'black'
      })

      let mipCarouselWrapper = popup.querySelector('.mip-carousel-wrapper')
      /* istanbul ignore if */
      if (mipCarouselWrapper == null) return

      // 找出当前视口下的图片
      let currentImg = getCurrentImg(mipCarouselWrapper, mipCarousel)
      popupImg.setAttribute('src', currentImg.getAttribute('data-src'))
      let previousPos = getImgOffset(img)
      // 获取弹出图片滑动的距离，根据前面的设定，top大于0就不是长图，小于0才是滑动的距离。
      let currentImgPos = getImgOffset(currentImg)
      currentImgPos.top < 0 && (previousPos.top -= currentImgPos.top)
      currentImgPos.left < 0 && (previousPos.left -= currentImgPos.left)
      css(popupImg, getPopupImgPos(popupImg.naturalWidth, popupImg.naturalHeight))
      css(popupImg, 'display', 'block')
      css(mipCarousel, 'display', 'none')
      naboo.animate(popupBg, {
        opacity: 0
      }).start()

      naboo.animate(popup, {'display': 'none'})
      naboo.animate(popupImg, previousPos).start(() => {
        css(img, 'visibility', 'visible')
        css(popup, 'display', 'none')
        popup.removeEventListener('click', imagePop, false)
        popup.remove()
      })
    }

    let onResize = function () {
      imgOffset = getImgOffset(img)
      css(popupImg, imgOffset)
      naboo.animate(popupImg, getPopupImgPos(img.naturalWidth, img.naturalHeight)).start()
    }
    window.addEventListener('resize', onResize)

    css(popupImg, imgOffset)
    css(mipCarousel, 'visibility', 'hidden')
    css(popupBg, 'opacity', 1)

    naboo.animate(popupImg, getPopupImgPos(img.naturalWidth, img.naturalHeight)).start(() => {
      css(popupImg, 'display', 'none')
      css(mipCarousel, 'visibility', 'visible')
    })
    css(img, 'visibility', 'hidden')
    css(img.parentNode, 'zIndex', 'inherit')
  }, false)
}