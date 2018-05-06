# Yet Another Webfront for STV2k Researching
> [PAMI Centre](http://pami.xmu.edu.cn), Xiamen University

Actually there's no other webfront, so this repo should not be a 'Yet Another'.
Anyhow, this is a web project written for visualizing and dashboarding STV2k Researching, since it's a Computer Vision project which deals with loads of images and captions.

### Dependency

The tech stack will be using:

+ [Caddy](https://caddyserver.com)
+ [Python 3.x](https://python.org)
+ [Flask](http://flask.pocoo.org/)
+ [Bootstrap](http://getbootstrap.com)
+ [uWSGI](https://github.com/unbit/uwsgi)

Evaluating the following plugins/frameworks/tools:

+ [Hugo](http://gohugo.io)

<del>And yes there may not be a fancy front framework, but we may choose [Semantic UI](https://semantic-ui.com/) if in mood : ) </del> Maybe cannot do due to NodeJS dependency which is out of our tech stack and [SUI's so-called CSS version](https://github.com/Semantic-Org/Semantic-UI-CSS) seems to be not pure CSS. 

However the interacting and visualizing ability will come first and related tech stack is still under consideration.

### Caddy Directives/Middlewares

Caddy comes with the following extra directives/middlewares:

| Name                                     | Status                |
| ---------------------------------------- | --------------------- |
| [filemanager](https://henriquedias.com/filemanager/caddy/) | **In Use**            |
| [authz](https://github.com/casbin/caddy-authz) | Not Active            |
| [cache](https://github.com/nicolasazrak/caddy-cache) | *Planning Deployment* |
| [cors](https://github.com/captncraig/cors) | Not Active            |
| [datadog](https://github.com/payintech/caddy-datadog) | Not Active            |
| [expires](https://github.com/epicagency/caddy-expires) | Evaluating            |
| [filter](https://github.com/echocat/caddy-filter) | Evaluating            |
| [git](https://github.com/abiosoft/caddy-git) | *Planning Deployment* |
| [hugo](https://gohugo.io/)               | Evaluating            |
| [ipfilter](https://github.com/pyed/ipfilter) | *Planning Deployment* |
| [jwt](https://github.com/BTBurke/caddy-jwt) | Not Active            |
| [locale](https://github.com/simia-tech/caddy-locale) | Not Active            |
| [login](https://github.com/tarent/loginsrv/tree/master/caddy) | Not Active            |
| [mailout](https://github.com/SchumacherFM/mailout) | Not Active            |
| [minify](https://github.com/hacdias/caddy-minify) | *Planning Deployment* |
| [nobots](https://github.com/Xumeiquer/nobots) | *Planning Deployment* |
| [ratelimit](https://github.com/xuqingfeng/caddy-rate-limit) | *Planning Deployment* |
| [realip](https://github.com/captncraig/caddy-realip) | *Planning Deployment* |
| [reauth](https://github.com/freman/caddy-reauth) | Not Active            |
| [upload](https://github.com/wmark/caddy.upload) | Evaluating            |
| [net (Server Type)](https://github.com/pieterlouw/caddy-net) | **In Use**            |
| [hook.service (Event Hook)](https://github.com/bruhs/caddy-service) | *Planning Deployment* |

Check [Caddy Userguide](https://caddyserver.com/docs) for details.
