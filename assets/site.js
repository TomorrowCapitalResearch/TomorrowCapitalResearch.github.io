/** Tomorrow Capital Research — dependency-free interactions.
 * Canvas imagery is conceptual and is never presented as observed market data. */
(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  const arrow = () => '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" class="arrow-icon"><path d="M5 19 19 5M8 5h11v11"/></svg>';
  document.querySelectorAll('[data-arrow]').forEach(el => el.innerHTML = arrow());
  document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');
  if (toggle && menu) {
    const setMenu = open => {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.textContent = open ? 'Close' : 'Menu';
      menu.classList.toggle('is-open', open);
      document.body.classList.toggle('nav-open', open && window.innerWidth <= 800);
    };
    toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
    window.addEventListener('keydown', e => {if (e.key === 'Escape') setMenu(false);});
    window.addEventListener('resize', () => {if (innerWidth > 800) setMenu(false);});
  }

  const reveals = [...document.querySelectorAll('[data-reveal]')];
  if (motionQuery.matches || !('IntersectionObserver' in window)) reveals.forEach(el => el.classList.add('visible'));
  else {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {if (e.isIntersecting) {e.target.classList.add('visible');io.unobserve(e.target);}});
    }, {threshold:.09,rootMargin:'0px 0px -30px 0px'});
    reveals.forEach(el => io.observe(el));
  }

  // Layered, interacting wavefronts. No circles, concentric rings or ornamental orbit paths.
  class WaveField {
    constructor(canvas) {
      this.canvas = canvas; this.ctx = canvas.getContext('2d', {alpha:true});
      if (!this.ctx) return;
      this.parent = canvas.parentElement;
      this.variant = canvas.dataset.wave || 'hero';
      this.reduced = motionQuery.matches; this.running = false; this.visible = true;
      this.last = 0; this.frame = 0; this.width = 0; this.height = 0;
      this.resize = this.resize.bind(this); this.tick = this.tick.bind(this);
      this.resize();
      this.ro = new ResizeObserver(this.resize);this.ro.observe(this.parent);
      if ('IntersectionObserver' in window) {
        this.io = new IntersectionObserver(entries => {this.visible = entries[0].isIntersecting;if(this.visible)this.start();else this.stop();}, {threshold:0});
        this.io.observe(canvas);
      }
      this.onVisibility = () => document.hidden ? this.stop() : this.start();
      document.addEventListener('visibilitychange',this.onVisibility);
      motionQuery.addEventListener?.('change', e => {this.reduced=e.matches;if(e.matches){this.stop();this.draw(0);}else this.start();});
      this.start();
    }
    resize(){
      const box = this.parent.getBoundingClientRect();
      this.width = Math.max(1,box.width);this.height = Math.max(1,box.height);
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      this.canvas.width = Math.round(this.width * ratio);this.canvas.height = Math.round(this.height * ratio);
      this.ctx.setTransform(ratio,0,0,ratio,0,0);
      this.draw(this.frame || 0);
    }
    draw(t){
      const g = this.ctx,w=this.width,h=this.height;
      g.clearRect(0,0,w,h);
      const isHero=this.variant==='hero',isPanel=this.variant==='panel';
      const lines=isHero?62:(isPanel?48:35);
      const left=isHero?w*.28:0;
      const right=w+15;
      const base=isHero?h*.57:h*.53;
      const span=isHero?h*.68:h*.63;
      const intensity=isHero?39:isPanel?39:31;
      // Fine multiple sine modes with spatially varying phase and envelope.
      // Nearby wavefronts are coupled through a shared displacement field.
      for(let n=0;n<lines;n++){
        const q=n/(lines-1), yBase=base+(q-.5)*span;
        const tint=Math.abs(q-.52);
        const color=n%11===0 ? `rgba(207,177,121,${isHero?.30:.38})` : `rgba(145,188,211,${(isHero?.14:.17)*(1-tint*.95)})`;
        g.beginPath();g.strokeStyle=color;g.lineWidth=n%11===0?1:.63;
        let drawn=false;
        for(let x=left;x<=right;x+=5){
          const u=x/w;
          const envelope=Math.exp(-Math.pow((u-.71)*2.15,2))*(0.55+0.45*Math.sin(Math.PI*q));
          const m1=Math.sin(u*8.6 - t*.38 + q*2.0);
          const m2=.43*Math.sin(u*17.9 + t*.24 - q*2.8);
          const m3=.18*Math.sin(u*34.2 - t*.15 + q*7.3);
          const coupling=6.5*Math.sin((q-.5)*7.8 + u*5.8 - t*.21);
          const y=yBase+(m1+m2+m3)*intensity*envelope + coupling*envelope;
          if(!drawn){g.moveTo(x,y);drawn=true;} else g.lineTo(x,y);
        }
        g.stroke();
      }
      // Wave energy, shown as a thin gold equilibrium trace, not a ring.
      const ey=base+5;
      g.beginPath();g.lineWidth=1;g.strokeStyle='rgba(211,179,119,.36)';
      for(let x=left;x<right;x+=5){
        const u=x/w, e=Math.exp(-Math.pow((u-.71)*2.15,2));
        const y=ey + e*24*Math.sin(8.6*u-t*.38) + e*8*Math.sin(17.9*u+t*.24);
        x===left?g.moveTo(x,y):g.lineTo(x,y);
      }
      g.stroke();
    }
    tick(now){
      if(!this.running)return;
      if(now-this.last>=33){this.last=now;this.frame=now/1000;this.draw(this.frame);}
      this.raf=requestAnimationFrame(this.tick);
    }
    start(){if(this.running||this.reduced||!this.visible||document.hidden)return;this.running=true;this.raf=requestAnimationFrame(this.tick);}
    stop(){this.running=false;cancelAnimationFrame(this.raf);}
  }
  document.querySelectorAll('canvas[data-wave]').forEach(el=>new WaveField(el));

  class EquilibriumLab {
    constructor(root){
      this.root=root;this.canvas=root.querySelector('canvas');this.ctx=this.canvas?.getContext('2d');if(!this.ctx)return;
      this.kInput=root.querySelector('[data-coupling]');this.dInput=root.querySelector('[data-damping]');
      this.kOut=root.querySelector('[data-coupling-output]');this.dOut=root.querySelector('[data-damping-output]');
      this.size=240;this.u=new Float32Array(this.size);this.v=new Float32Array(this.size);
      this.time=0;this.running=false;this.reduced=motionQuery.matches;this.visible=true;
      this.shock(1);this.resize();
      this.ro=new ResizeObserver(()=>this.resize());this.ro.observe(this.canvas.parentElement);
      this.kInput?.addEventListener('input',()=>this.setLabels());this.dInput?.addEventListener('input',()=>this.setLabels());
      root.querySelector('[data-shock]')?.addEventListener('click',()=>{this.shock(1);this.draw();this.start();});
      root.querySelector('[data-reset]')?.addEventListener('click',()=>{this.u.fill(0);this.v.fill(0);this.draw();});
      if ('IntersectionObserver' in window){this.io=new IntersectionObserver(e=>{this.visible=e[0].isIntersecting;this.visible?this.start():this.stop();});this.io.observe(root);}
      document.addEventListener('visibilitychange',()=>document.hidden?this.stop():this.start());
      motionQuery.addEventListener?.('change',e=>{this.reduced=e.matches;if(e.matches){this.stop();this.draw();}else this.start();});
      this.setLabels();this.draw();this.start();
    }
    setLabels(){if(this.kOut)this.kOut.textContent=(+this.kInput.value).toFixed(2);if(this.dOut)this.dOut.textContent=(+this.dInput.value).toFixed(2);}
    shock(amplitude){const center=Math.floor(this.size*.43);for(let i=1;i<this.size-1;i++){const r=(i-center)/13;this.u[i]+=amplitude*Math.exp(-.5*r*r);}}
    resize(){const b=this.canvas.parentElement.getBoundingClientRect(),d=Math.min(devicePixelRatio||1,2);this.w=Math.max(b.width,1);this.h=Math.max(b.height,1);this.canvas.width=this.w*d;this.canvas.height=this.h*d;this.ctx.setTransform(d,0,0,d,0,0);this.draw();}
    evolve(){const k=+this.kInput.value, damping=+this.dInput.value;for(let j=0;j<5;j++){
      const dt=.25;
      for(let i=1;i<this.size-1;i++){const lap=this.u[i-1]+this.u[i+1]-2*this.u[i];this.v[i]+=(k*lap-damping*this.v[i])*dt;}
      for(let i=1;i<this.size-1;i++)this.u[i]+=this.v[i]*dt;
      this.u[0]=0;this.u[this.size-1]=0;
    }this.time++;}
    draw(){if(!this.ctx)return;const g=this.ctx,w=this.w||1,h=this.h||1;g.clearRect(0,0,w,h);
      g.strokeStyle='rgba(184,207,221,.07)';g.lineWidth=1;
      for(let y=40;y<h;y+=40){g.beginPath();g.moveTo(0,y);g.lineTo(w,y);g.stroke();}
      for(let x=0;x<w;x+=45){g.beginPath();g.moveTo(x,0);g.lineTo(x,h);g.stroke();}
      g.strokeStyle='rgba(198,168,113,.27)';g.beginPath();g.moveTo(0,h*.56);g.lineTo(w,h*.56);g.stroke();
      const center=h*.56, amp=Math.min(92,h*.35);
      // Transparent offset wavefront layers show propagation and coupling.
      for(let layer=5;layer>=0;layer--){g.beginPath();g.strokeStyle=layer===0?'rgba(226,202,152,.96)':`rgba(135,177,206,${.12+(5-layer)*.04})`;g.lineWidth=layer===0?2.1:1.1;
      const off=(layer/5-.5)*28;
      for(let i=0;i<this.size;i++){const x=i/(this.size-1)*w,y=center+off-this.u[i]*amp*(1+layer*.05);i===0?g.moveTo(x,y):g.lineTo(x,y);}g.stroke();}
    }
    tick(){if(!this.running)return;this.evolve();this.draw();this.raf=requestAnimationFrame(()=>this.tick());}
    start(){if(this.running||this.reduced||!this.visible||document.hidden)return;this.running=true;this.raf=requestAnimationFrame(()=>this.tick());}
    stop(){this.running=false;cancelAnimationFrame(this.raf);}
  }
  document.querySelectorAll('[data-equilibrium-lab]').forEach(root=>new EquilibriumLab(root));
})();
