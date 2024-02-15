<script lang="ts">
	import type { TextWidget } from "../../../client";

    export let widget: TextWidget
</script>

<div class="bg-slate-400 p-4 shadow-md">
    {widget.text}
</div>