import { useState } from 'react'
import { Button } from "/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "/components/ui/card"
import { Input } from "/components/ui/input"
import { Label } from "/components/ui/label"
import { Clock, Heart, Plus } from 'lucide-react'

type Activity = {
  id: string
  type: string
  duration: number
  date: string
}

export default function FitnessTracker() {
  const [activities, setActivities] = useState<Activity[]>([])
  const [activityType, setActivityType] = useState('')
  const [duration, setDuration] = useState('')
  const [date, setDate] = useState('')
  const [showForm, setShowForm] = useState(false)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!activityType || !duration || !date) return

    const newActivity: Activity = {
      id: Date.now().toString(),
      type: activityType,
      duration: parseInt(duration),
      date: date
    }

    setActivities([...activities, newActivity])
    setActivityType('')
    setDuration('')
    setDate('')
    setShowForm(false)
  }

  const totalDuration = activities.reduce((sum, activity) => sum + activity.duration, 0)
  const totalActivities = activities.length

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-2xl mx-auto">
        <Card className="mb-6">
          <CardHeader>
            <CardTitle className="text-2xl font-bold flex items-center gap-2">
              <Heart className="text-red-500" /> Fitness Tracker
            </CardTitle>
            <CardDescription>
              Track your daily activities and monitor your progress
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 gap-4 mb-6">
              <Card>
                <CardHeader className="pb-2">
                  <CardDescription>Total Activities</CardDescription>
                  <CardTitle className="text-3xl">{totalActivities}</CardTitle>
                </CardHeader>
              </Card>
              <Card>
                <CardHeader className="pb-2">
                  <CardDescription>Total Minutes</CardDescription>
                  <CardTitle className="text-3xl">{totalDuration}</CardTitle>
                </CardHeader>
              </Card>
            </div>

            <Button onClick={() => setShowForm(!showForm)} className="w-full">
              <Plus className="mr-2 h-4 w-4" /> Log New Activity
            </Button>
          </CardContent>
        </Card>

        {showForm && (
          <Card className="mb-6">
            <CardHeader>
              <CardTitle>Log Activity</CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="space-y-2">
                  <Label htmlFor="type">Activity Type</Label>
                  <Input
                    id="type"
                    value={activityType}
                    onChange={(e) => setActivityType(e.target.value)}
                    placeholder="e.g. Running, Cycling"
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="duration">Duration (minutes)</Label>
                  <Input
                    id="duration"
                    type="number"
                    value={duration}
                    onChange={(e) => setDuration(e.target.value)}
                    placeholder="30"
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="date">Date</Label>
                  <Input
                    id="date"
                    type="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                  />
                </div>
                <Button type="submit" className="w-full">
                  Save Activity
                </Button>
              </form>
            </CardContent>
          </Card>
        )}

        <Card>
          <CardHeader>
            <CardTitle>Activity History</CardTitle>
          </CardHeader>
          <CardContent>
            {activities.length === 0 ? (
              <p className="text-gray-500 text-center py-4">No activities logged yet</p>
            ) : (
              <div className="space-y-4">
                {activities.map((activity) => (
                  <Card key={activity.id}>
                    <CardContent className="pt-4">
                      <div className="flex justify-between items-center">
                        <div>
                          <h3 className="font-medium">{activity.type}</h3>
                          <p className="text-sm text-gray-500">{activity.date}</p>
                        </div>
                        <div className="flex items-center gap-1">
                          <Clock className="h-4 w-4 text-gray-500" />
                          <span>{activity.duration} min</span>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                ))}
