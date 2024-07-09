document.addEventListener("DOMContentLoaded", function() {
    let currentURL = window.location.pathname;
    currentURL = "item-" + currentURL.slice(1).replace('/','-')
    let currentEl = document.querySelector(`.${currentURL}`).id="active"
    let activeItemIndicator = CSSRulePlugin.getRule(`.menu-item p#active:after`);
    const toggleButton = document.querySelector(".burger");
    const bodyEl = document.querySelector("body")

    let isOpen = false;

    gsap.set(".menu-item p", {y : 425});
    const timeline = gsap.timeline({paused: true});


    timeline.to(".overlay", {
        visibility: "visible",
        duration: 0.50,
        clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)",
        ease: "power4.inOut"
    });

    timeline.to(".menu-item p", {
        y: 0,
        ease: "power4.out"
    }, "-=1");

    timeline.to(activeItemIndicator, {
        width: "100%",
        duration: 0.75,
        ease: "power4.out",
        delay: 0.5,
    }, "<");

    toggleButton.addEventListener("click", function() {
        if (isOpen){
            timeline.reverse();
            console.log("CLOSEOPEN");
            bodyEl.style.overflowY = "visible";
            
        } else{
            timeline.play();
            console.log("NOWOPEN");
            bodyEl.style.overflowY = "hidden";
        }
        isOpen = !isOpen;
    })
})