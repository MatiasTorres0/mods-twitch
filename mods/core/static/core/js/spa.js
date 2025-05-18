document.addEventListener('DOMContentLoaded', function() {
    // Inicializar la aplicación
    initApp();
    
    // Manejar la navegación
    document.addEventListener('click', function(e) {
        // Buscar enlaces con el atributo data-link
        const link = e.target.closest('[data-link]');
        if (link) {
            e.preventDefault();
            navigateTo(link.href);
            
            // Actualizar la clase active en la barra de navegación
            updateActiveNavLink(link.getAttribute('data-page'));
        }
    });
    
    // Manejar eventos de navegación del navegador
    window.addEventListener('popstate', function() {
        loadContent(window.location.pathname);
    });
    
    // Inicializar la aplicación
    function initApp() {
        // Cargar el contenido inicial basado en la URL actual
        loadContent(window.location.pathname);
        
        // Establecer el enlace activo inicial
        const currentPath = window.location.pathname;
        const currentPage = getPageNameFromPath(currentPath);
        updateActiveNavLink(currentPage);
    }
    
    // Navegar a una URL
    function navigateTo(url) {
        // Actualizar la historia del navegador
        history.pushState(null, null, url);
        
        // Cargar el contenido
        loadContent(url);
    }
    
    // Cargar contenido de forma asíncrona
    function loadContent(url) {
        // Mostrar indicador de carga
        const appContent = document.getElementById('app-content');
        appContent.innerHTML = '<div class="container text-center py-5"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Cargando...</span></div></div>';
        
        // Realizar solicitud AJAX para obtener el contenido
        fetch(url + '?ajax=true')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error de red: ' + response.status);
                }
                return response.text();
            })
            .then(html => {
                // Actualizar el contenido
                appContent.innerHTML = html;
                
                // Ejecutar scripts en el contenido cargado
                executeScripts(appContent);
            })
            .catch(error => {
                console.error('Error al cargar el contenido:', error);
                appContent.innerHTML = '<div class="container"><div class="alert alert-danger">Error al cargar el contenido. Por favor, intenta de nuevo.</div></div>';
            });
    }
    
    // Ejecutar scripts en el contenido cargado dinámicamente
    function executeScripts(container) {
        const scripts = container.querySelectorAll('script');
        scripts.forEach(oldScript => {
            const newScript = document.createElement('script');
            Array.from(oldScript.attributes).forEach(attr => {
                newScript.setAttribute(attr.name, attr.value);
            });
            newScript.textContent = oldScript.textContent;
            oldScript.parentNode.replaceChild(newScript, oldScript);
        });
    }
    
    // Actualizar el enlace activo en la barra de navegación
    function updateActiveNavLink(pageName) {
        // Quitar la clase active de todos los enlaces
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        
        // Añadir la clase active al enlace correspondiente
        const activeLink = document.querySelector(`.nav-link[data-page="${pageName}"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }
    }
    
    // Obtener el nombre de la página a partir de la ruta
    function getPageNameFromPath(path) {
        // Eliminar la barra inicial y final si existen
        path = path.replace(/^\/|\/$/g, '');
        
        // Dividir la ruta por barras y tomar el último segmento
        const segments = path.split('/');
        const lastSegment = segments[segments.length - 1];
        
        // Si el último segmento está vacío (por ejemplo, en '/'), usar 'inicio'
        return lastSegment || 'inicio';
    }
});