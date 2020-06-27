window.addEventListener('scroll',function(){
    const img = document.querySelector('.imgmove')
    let nowscroll = document.children[0].scrollTop
    nowscroll = Math.floor(nowscroll)
    img.style.transform = `translateY(-${nowscroll/4}px)`
    navbar(nowscroll)
    function navbar(scroll){
        const nav = document.querySelector('.navbar')
        if (scroll>400){
            nav.style.width = '100%'
            nav.style.position = "fixed"
        }else{
            nav.style.width = 'none'
            nav.style.position = "relative"
        }
    }
})

