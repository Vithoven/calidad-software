//change the limit to however many images to use
const url = `https://api.thecatapi.com/v1/images/search?limit=1`;
const api_key = "live_H3TNfGoQdFQhPWkHlUAUUjwsZUjHhhwDoz6jKyt1g9w6CV3lw6m7x0IQt4UkrMOg"

 fetch(url,{headers: {
      'x-api-key': api_key
    }})
 .then((response) => {
   return response.json();
 })
.then((data) => {
  let imagesData = data;
  imagesData.map(function(imageData) {
    
    let image = document.createElement('img');
    //use the url from the image object
    image.src = `${imageData.url}`;
    image.setAttribute("class" , "object-fit-contain ");
    image.setAttribute("height" , "250");
     
    document.getElementById('cat_img').appendChild(image);
    
    });
})
.catch(function(error) {
   console.log(error);
});