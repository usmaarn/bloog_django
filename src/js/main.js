import { createIcons } from 'lucide';
import {ThumbsUp, Bookmark, Share2, MoveRight } from "lucide";
import {Alpine} from "alpinejs";
import axios from "axios";

// Caution, this will import all the icons and bundle them.
createIcons({ icons: {
        ThumbsUp, Bookmark, Share2, MoveRight
    }, attrs: {
    class: ['lucide-icons', 'icon'],
    'stroke-width': 0.2,
    stroke: '#000'
  }, });

window.axios = axios
window.Alpine = Alpine

Alpine.data('comment', (url) => ({
    liked: false,
    async init(){
        let res = await axios.get(url)
        this.liked = res.data?.liked
    }
}))

Alpine.start()

