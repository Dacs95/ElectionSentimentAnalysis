import { Pie } from 'vue-chartjs'

export default {
  extends: Pie,
  props: ['datacollection', 'options'],
  mounted () {
    this.renderChart(this.datacollection, this.options,
      {responsive: true, maintainAspectRatio: false})
  }
}
