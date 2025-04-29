// "Infinite scroll" illusion via pagination links
window.addEventListener('scroll', () => {
  const nearBottom = window.innerHeight + window.scrollY >= document.body.offsetHeight - 200;
  const nextLink = document.querySelector('.pagination .next a');
  if (nearBottom && nextLink) {
    fetch(nextLink.href).then(r=>r.text()).then(html=>{
      const doc = new DOMParser().parseFromString(html,'text/html');
      const items = doc.querySelectorAll('.tool-item');
      items.forEach(item => document.querySelector('.tool-list').appendChild(item));
      document.querySelector('.pagination').innerHTML = doc.querySelector('.pagination').innerHTML;
    });
  }
});
